from django.shortcuts import render

job_dicts = {
  'Accounting & Finance': ['Accountant', 'Financial Analyst', 'Auditor', 'Tax Specialist'],
  'Admin & Office Support': ['Executive Assistant', 'Office Manager', 'Receptionist', 'Data Entry Clerk'],
  'Agriculture, Forestry & Fishing': ['Agricultural Scientist', 'Fisheries Scientist', 'Forester', 'Agricultural Engineer'],
  'Architecture & Building': ['Architect', 'Building Designer', 'Urban Planner', 'Construction Manager'],
  'Arts, Design, Entertainment & Media': ['Graphic Designer', 'Artist', 'Photographer', 'Video Editor'],
  'Banking, Insurance & Real Estate': ['Financial Analyst', 'Credit Analyst', 'Loan Officer', 'Real Estate Broker'],
  'Business & Management': ['Business Manager', 'Operations Manager', 'Human Resources Manager', 'Sales Manager'],
  'Business, Management & Commerce': ['Business Manager', 'Operations Manager', 'Human Resources Manager', 'Sales Manager'],
}

# Create your views here.
def job_list(request):
  return render(request, 'jobs/job_list.html', {
    'jobs': job_dicts
  })