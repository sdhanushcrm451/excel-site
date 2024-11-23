from django.shortcuts import render, redirect
from django.http import HttpResponse
import openpyxl
import os
from django.conf import settings

def start_session(request):
    """Start the session and set field names."""
    if request.method == 'POST':
        # Get the field names from the form
        field_names = request.POST.getlist('field_names[]')
        
        # Ensure field names are provided
        if not field_names:
            return HttpResponse("No field names provided. Please go back and try again.")

        # Save field names to session
        request.session['field_names'] = field_names

        # Create an Excel file with headings
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.append(field_names)
        workbook.save('data.xlsx')

        # Redirect to the next step (add_values page)
        return redirect('add_values')
    
    return render(request, 'start_session.html')

def add_values(request):
    """Handle form submission and add values to an Excel file."""
    if request.method == 'POST':
        field_names = request.session.get('field_names', [])
        if field_names:
            # Create a new workbook or open an existing one
            workbook = openpyxl.load_workbook('data.xlsx')
            sheet = workbook.active

            # Add the submitted values to the Excel sheet
            row = [request.POST.get(field) for field in field_names]
            sheet.append(row)
            workbook.save('data.xlsx')

            # After successfully adding the values, redirect to a confirmation page
            return redirect('value_added')  # You can create a new page for this.

    return render(request, 'add_values.html', {'field_names': request.session.get('field_names', [])})

def value_added(request):
    """Display the 'Value Added' confirmation page."""
    return render(request, 'value_added.html')

# Your session-end view
def end_session(request):
    # Path to the saved Excel file
    excel_file_path = os.path.join(settings.BASE_DIR, 'data.xlsx')

    # Check if the file exists
    if os.path.exists(excel_file_path):
        return render(request, 'session_ended.html', {'file_exists': True})
    else:
        return render(request, 'session_ended.html', {'file_exists': False})

# View to handle file download

def download_excel(request):
    # Path to the saved Excel file
    excel_file_path = os.path.join(settings.BASE_DIR, 'data.xlsx')

    if os.path.exists(excel_file_path):
        with open(excel_file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename="data.xlsx"'
            return response
    else:
        return HttpResponse("File not found", status=404)