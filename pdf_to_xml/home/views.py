from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import LcData
from .forms import LcDataUploadForm
import fitz  # PyMuPDF
import re

# Create your views here.

def welcome(request):

    return render(request,'home.html')


def upload_pdf(request):

    extracted_lc_number = None
    extracted_date_of_issue = None
    extracted_date_of_expiry=None
    extracted_applicant=None
    extracted_beneficiary=None
    extracted_currency=None
    extracted_amount=None
    extracted_tenor=None
    extracted_ad=None


    transaction_form = LcDataUploadForm()

    if request.method == "POST" and request.FILES.get("pdf_file"):

        pdf_file = request.FILES["pdf_file"]  # Get the uploaded file

        # Read the PDF file directly from memory
        pdf_document = fitz.open(stream=pdf_file.read(), filetype="pdf")

        # Extract transaction reference
        
        for page in pdf_document:
            text = page.get_text("text")
            for line in text.split("\n"):
                if line.startswith(":20/TRANSACTION REFERENCE NUMBER"):
                    extracted_lc_number = line.split(":")[-1].strip()

                if line.startswith(":31C/Date of Issue"):
                    extracted_date_of_issue = line.split(":")[-1].strip()

                if line.startswith(":31D/Date and Place of Expiry"):
                    match = re.search(r": (\d{6})", line)
                    if match:
                        extracted_date_of_expiry= match.group(1)
                
                if line.startswith(":50/Applicant"):
                    parts = line.split(":")
                    if len(parts) > 2:
                        extracted_applicant = parts[2].strip()
                
                if line.startswith(":59/Beneficiary"):
                    parts = line.split(":")
                    if len(parts) > 2:
                        extracted_beneficiary = parts[2].strip()
                
                if line.startswith(":32B/CURRENCY CODE, AMOUNT"):
                    match = re.search(r": (\S{3})", line)
                    if match:
                        extracted_currency= match.group(1)
                
                if line.startswith(":32B/CURRENCY CODE, AMOUNT"):
                    match = re.search(r"[A-Z]{3}(\d+,\d+)", line)
                    if match:
                        extracted_amount= match.group(1)
                
                if line.startswith(":42C/Drafts at …"):
                    match = re.search(r": (\d+)", line)
                    if match:
                        extracted_tenor= match.group(1)
                
                if line.startswith("2:I700"):
                    match = re.search(r": (\S{8})", line)
                    if match:
                        extracted_ad= match.group(1)
                


        # Pre-fill the form with extracted data (if found)
        transaction_form = LcDataUploadForm(initial={"lc_number": extracted_lc_number,'date_of_issue':extracted_date_of_issue,'expiry_date':extracted_date_of_expiry,'applicant':extracted_applicant,'beneficiary':extracted_beneficiary,'currency':extracted_currency,'amount':extracted_amount,'tenor':extracted_tenor})

    return render(request, "upload_pdf.html", {
        "transaction_form": transaction_form,
        "extracted_lc_number": extracted_lc_number,
        'extracted_date_of_issue':extracted_date_of_issue,
        'extracted_date_of_expiry':extracted_date_of_expiry,
        'extracted_applicant':extracted_applicant,
        'extracted_beneficiary': extracted_beneficiary,
        'extracted_currency':extracted_currency,
        'extracted_amount':extracted_amount,
        'extracted_tenor': extracted_tenor,

    })

def save_transaction(request):
    if request.method == "POST":
        form = LcDataUploadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("upload_pdf")  # Redirect to the upload page after saving
    return redirect("upload_pdf")
