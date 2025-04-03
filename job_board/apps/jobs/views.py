from django.shortcuts import render

from django.shortcuts import render

job_dicts = [
    {
        'category': 'Accounting & Finance',
        'jobs': [
            {'title': 'Accountant', 'slug': 'accountant', 'salary': '$60,000 - $80,000', 'description': 'Manages financial records and ensures compliance with regulations.'},
            {'title': 'Financial Analyst', 'slug': 'financial-analyst', 'salary': '$70,000 - $95,000', 'description': 'Analyzes financial data to support business decisions.'},
            {'title': 'Auditor', 'slug': 'auditor', 'salary': '$65,000 - $85,000', 'description': 'Examines financial records for accuracy and compliance.'},
            {'title': 'Tax Specialist', 'slug': 'tax-specialist', 'salary': '$75,000 - $100,000', 'description': 'Provides expert advice on tax laws and regulations.'},
        ],
        'slug': 'accounting-finance',
    },
    {
        'category': 'Admin & Office Support',
        'jobs': [
            {'title': 'Executive Assistant', 'slug': 'executive-assistant', 'salary': '$50,000 - $70,000', 'description': 'Provides high-level administrative support to executives.'},
            {'title': 'Office Manager', 'slug': 'office-manager', 'salary': '$45,000 - $65,000', 'description': 'Oversees daily office operations and ensures efficiency.'},
            {'title': 'Receptionist', 'slug': 'receptionist', 'salary': '$30,000 - $40,000', 'description': 'Greets visitors and handles incoming calls and inquiries.'},
            {'title': 'Data Entry Clerk', 'slug': 'data-entry-clerk', 'salary': '$35,000 - $45,000', 'description': 'Enters and maintains accurate data in databases.'},
        ],
        'slug': 'admin-office-support',
    },
    {
        'category': 'Agriculture, Forestry & Fishing',
        'jobs': [
            {'title': 'Agricultural Scientist', 'slug': 'agricultural-scientist', 'salary': '$60,000 - $85,000', 'description': 'Conducts research to improve agricultural productivity.'},
            {'title': 'Fisheries Scientist', 'slug': 'fisheries-scientist', 'salary': '$55,000 - $80,000', 'description': 'Studies aquatic ecosystems and manages fish populations.'},
            {'title': 'Forester', 'slug': 'forester', 'salary': '$50,000 - $75,000', 'description': 'Manages forests for timber production and conservation.'},
            {'title': 'Agricultural Engineer', 'slug': 'agricultural-engineer', 'salary': '$65,000 - $90,000', 'description': 'Designs and develops agricultural machinery and systems.'},
        ],
        'slug': 'agriculture-forestry-fishing',
    },
    {
        'category': 'Architecture & Building',
        'jobs': [
            {'title': 'Architect', 'slug': 'architect', 'salary': '$100,000', 'description': 'Designs buildings and oversees construction projects.'},
            {'title': 'Building Designer', 'slug': 'building-designer', 'salary': '$80,000', 'description': 'Creates detailed plans and drawings for buildings.'},
            {'title': 'Urban Planner', 'slug': 'urban-planner', 'salary': '$90,000', 'description': 'Develops plans for land use and community development.'},
            {'title': 'Construction Manager', 'slug': 'construction-manager', 'salary': '$120,000', 'description': 'Manages construction projects and ensures timely completion.'},
        ],
        'slug': 'architecture-building',
    },
    {
        'category': 'Arts, Design, Entertainment & Media',
        'jobs': [
            {'title': 'Graphic Designer', 'slug': 'graphic-designer', 'salary': '$50,000 - $70,000', 'description': 'Creates visual concepts for marketing and branding.'},
            {'title': 'Artist', 'slug': 'artist', 'salary': '$40,000 - $60,000', 'description': 'Creates original artwork for various purposes.'},
            {'title': 'Photographer', 'slug': 'photographer', 'salary': '$45,000 - $65,000', 'description': 'Captures images for commercial and artistic purposes.'},
            {'title': 'Video Editor', 'slug': 'video-editor', 'salary': '$55,000 - $75,000', 'description': 'Edits and assembles video footage for various media.'},
        ],
        'slug': 'arts-design-entertainment-media',
    },
    {
        'category': 'Banking, Insurance & Real Estate',
        'jobs': [
            {'title': 'Financial Analyst', 'slug': 'financial-analyst-banking', 'salary': '$70,000 - $95,000', 'description': 'Analyzes financial data for banking and investment decisions.'},
            {'title': 'Credit Analyst', 'slug': 'credit-analyst', 'salary': '$65,000 - $85,000', 'description': 'Evaluates creditworthiness of individuals and businesses.'},
            {'title': 'Loan Officer', 'slug': 'loan-officer', 'salary': '$60,000 - $80,000', 'description': 'Assists clients with loan applications and approvals.'},
            {'title': 'Real Estate Broker', 'slug': 'real-estate-broker', 'salary': '$75,000 - $100,000', 'description': 'Facilitates real estate transactions and negotiations.'},
        ],
        'slug': 'banking-insurance-real-estate',
    },
    {
        'category': 'Business & Management',
        'jobs': [
            {'title': 'Business Manager', 'slug': 'business-manager', 'salary': '$80,000 - $110,000', 'description': 'Oversees business operations and ensures profitability.'},
            {'title': 'Operations Manager', 'slug': 'operations-manager', 'salary': '$75,000 - $100,000', 'description': 'Manages day-to-day operations and improves efficiency.'},
            {'title': 'Human Resources Manager', 'slug': 'human-resources-manager', 'salary': '$85,000 - $120,000', 'description': 'Manages recruitment, employee relations, and HR policies.'},
            {'title': 'Sales Manager', 'slug': 'sales-manager', 'salary': '$90,000 - $130,000', 'description': 'Leads sales teams and develops sales strategies.'},
        ],
        'slug': 'business-management',
    },
    {
        'category': 'Business, Management & Commerce',
        'jobs': [
            {'title': 'Business Manager', 'slug': 'business-manager-commerce', 'salary': '$80,000 - $110,000', 'description': 'Oversees business operations and ensures profitability in commerce.'},
            {'title': 'Operations Manager', 'slug': 'operations-manager-commerce', 'salary': '$75,000 - $100,000', 'description': 'Manages day-to-day operations and improves efficiency in commerce.'},
            {'title': 'Human Resources Manager', 'slug': 'human-resources-manager-commerce', 'salary': '$85,000 - $120,000', 'description': 'Manages recruitment, employee relations, and HR policies in commerce.'},
            {'title': 'Sales Manager', 'slug': 'sales-manager-commerce', 'salary': '$90,000 - $130,000', 'description': 'Leads sales teams and develops sales strategies in commerce.'},
        ],
        'slug': 'business-management-commerce',
    },
]

# Create your views here.
def job_list(request): 
  return render(request, 'jobs/job_list.html', {
    'job_dicts': job_dicts
  })

def job_detail(request, slug):
    selected_job = None
    for job_data in job_dicts:
        for job in job_data['jobs']:
            if job['slug'] == slug:
                selected_job = job
                break  # Break out of the inner loop
        if selected_job:
            break  # Break out of the outer loop

    return render(request, 'jobs/job_detail.html', {
        'job': selected_job
    })