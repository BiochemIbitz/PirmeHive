from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime

def home(request):
    services = [
        {
            'id': 'web-development',
            'title': 'Web Development',
            'description': 'Transform your ideas into powerful web applications with our expert web development services.',
            'icon': 'fas fa-code',
            'short_description': 'Custom web applications tailored to your needs'
        },
        {
            'id': 'mobile-development',
            'title': 'Mobile Development',
            'description': 'Create powerful mobile applications for iOS and Android platforms.',
            'icon': 'fas fa-mobile-alt',
            'short_description': 'Native and cross-platform mobile applications'
        },
        {
            'id': 'cloud-solutions',
            'title': 'Cloud Solutions',
            'description': 'Scalable and secure cloud infrastructure for your business.',
            'icon': 'fas fa-cloud',
            'short_description': 'Scalable cloud infrastructure and deployment'
        },
        {
            'id': 'ui-ux-design',
            'title': 'UI/UX Design',
            'description': 'Create beautiful and intuitive user experiences.',
            'icon': 'fas fa-paint-brush',
            'short_description': 'Beautiful and intuitive user interfaces'
        },
        {
            'id': 'ai-robotics',
            'title': 'AI & Robotics',
            'description': 'Harness the power of artificial intelligence and robotics for your business.',
            'icon': 'fas fa-robot',
            'short_description': 'Advanced AI solutions and robotic systems'
        }
    ]
    return render(request, 'core/home.html', {'services': services})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        department = request.POST.get('department')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Determine department email based on selection
        department_emails = {
            'software': 'software@primehive.com',
            'ai-robotics': 'ai-robotics@primehive.com',
            'web-design': 'web-design@primehive.com',
            'project': 'project@primehive.com',
            'client-services': 'clients@primehive.com',
            'qa': 'qa@primehive.com',
            'hr': 'hr@primehive.com',
            'finance': 'finance@primehive.com',
            'marketing': 'marketing@primehive.com'
        }

        department_email = department_emails.get(department, 'info@primehive.com')
        
        email_message = f"""
        New contact form submission:
        
        Name: {name}
        Email: {email}
        Department: {department}
        Subject: {subject}
        
        Message:
        {message}
        """

        try:
            send_mail(
                f'Contact Form: {subject}',
                email_message,
                settings.DEFAULT_FROM_EMAIL,
                [department_email],
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent successfully. We will contact you soon.')
        except Exception as e:
            messages.error(request, 'There was an error sending your message. Please try again later.')
        
        return redirect('contact')
    
    return render(request, 'core/contact.html')

def service_detail(request, service_id):
    services_data = {
        'web-development': {
            'id': 'web-development',
            'title': 'Web Development',
            'description': 'Transform your ideas into powerful web applications with our expert web development services.',
            'icon': 'fas fa-code',
            'features': [
                {
                    'title': 'Custom Web Applications',
                    'description': 'Tailored solutions built with modern frameworks and technologies.'
                },
                {
                    'title': 'E-commerce Solutions',
                    'description': 'Secure and scalable online stores with payment integration.'
                },
                {
                    'title': 'Content Management Systems',
                    'description': 'Easy-to-use CMS for managing your website content.'
                },
                {
                    'title': 'API Development',
                    'description': 'RESTful APIs for seamless integration with other services.'
                }
            ],
            'pricing_plans': [
                {
                    'name': 'Basic',
                    'price': '999',
                    'period': 'project',
                    'features': [
                        'Up to 5 Pages',
                        'Responsive Design',
                        'Basic SEO',
                        '1 Month Support'
                    ]
                },
                {
                    'name': 'Professional',
                    'price': '2499',
                    'period': 'project',
                    'recommended': True,
                    'features': [
                        'Up to 10 Pages',
                        'Advanced Features',
                        'CMS Integration',
                        '3 Months Support'
                    ]
                },
                {
                    'name': 'Enterprise',
                    'price': '4999',
                    'period': 'project',
                    'features': [
                        'Unlimited Pages',
                        'Custom Features',
                        'Priority Support',
                        '6 Months Support'
                    ]
                }
            ],
            'process_steps': [
                {
                    'title': 'Requirements Gathering',
                    'description': 'We work with you to understand your needs and goals.'
                },
                {
                    'title': 'Design & Planning',
                    'description': 'Creating wireframes and technical specifications.'
                },
                {
                    'title': 'Development',
                    'description': 'Building your application with regular updates.'
                },
                {
                    'title': 'Testing & Launch',
                    'description': 'Thorough testing and smooth deployment.'
                }
            ]
        },
        'mobile-development': {
            'id': 'mobile-development',
            'title': 'Mobile Development',
            'description': 'Create powerful mobile applications for iOS and Android platforms.',
            'icon': 'fas fa-mobile-alt',
            'features': [
                {
                    'title': 'Native Applications',
                    'description': 'High-performance apps built specifically for iOS and Android.'
                },
                {
                    'title': 'Cross-Platform Development',
                    'description': 'Cost-effective solutions that work on multiple platforms.'
                },
                {
                    'title': 'App Store Optimization',
                    'description': 'Maximize your app\'s visibility and downloads.'
                },
                {
                    'title': 'Mobile UI/UX Design',
                    'description': 'Intuitive and engaging user interfaces.'
                }
            ],
            'pricing_plans': [
                {
                    'name': 'Basic',
                    'price': '2999',
                    'period': 'project',
                    'features': [
                        'Single Platform',
                        'Basic Features',
                        'App Store Submission',
                        '1 Month Support'
                    ]
                },
                {
                    'name': 'Professional',
                    'price': '5999',
                    'period': 'project',
                    'recommended': True,
                    'features': [
                        'Both Platforms',
                        'Advanced Features',
                        'Analytics Integration',
                        '3 Months Support'
                    ]
                },
                {
                    'name': 'Enterprise',
                    'price': '9999',
                    'period': 'project',
                    'features': [
                        'Custom Features',
                        'Backend Integration',
                        'Priority Support',
                        '6 Months Support'
                    ]
                }
            ],
            'process_steps': [
                {
                    'title': 'Strategy & Planning',
                    'description': 'Defining app features and technical requirements.'
                },
                {
                    'title': 'UI/UX Design',
                    'description': 'Creating intuitive and engaging interfaces.'
                },
                {
                    'title': 'Development & Testing',
                    'description': 'Building and testing your application.'
                },
                {
                    'title': 'Launch & Marketing',
                    'description': 'App store submission and promotion.'
                }
            ]
        },
        'cloud-solutions': {
            'id': 'cloud-solutions',
            'title': 'Cloud Solutions',
            'description': 'Scalable and secure cloud infrastructure for your business.',
            'icon': 'fas fa-cloud',
            'features': [
                {
                    'title': 'Cloud Migration',
                    'description': 'Seamless transition to cloud platforms.'
                },
                {
                    'title': 'Infrastructure Management',
                    'description': 'Monitoring and optimization of cloud resources.'
                },
                {
                    'title': 'Security & Compliance',
                    'description': 'Industry-standard security practices.'
                },
                {
                    'title': 'Disaster Recovery',
                    'description': 'Backup and recovery solutions.'
                }
            ],
            'pricing_plans': [
                {
                    'name': 'Starter',
                    'price': '499',
                    'period': 'month',
                    'features': [
                        'Basic Monitoring',
                        'Email Support',
                        'Daily Backups',
                        'Basic Security'
                    ]
                },
                {
                    'name': 'Business',
                    'price': '999',
                    'period': 'month',
                    'recommended': True,
                    'features': [
                        '24/7 Monitoring',
                        'Priority Support',
                        'Hourly Backups',
                        'Advanced Security'
                    ]
                },
                {
                    'name': 'Enterprise',
                    'price': '1999',
                    'period': 'month',
                    'features': [
                        'Custom Solutions',
                        'Dedicated Support',
                        'Custom Backup Plans',
                        'Enterprise Security'
                    ]
                }
            ],
            'process_steps': [
                {
                    'title': 'Assessment',
                    'description': 'Evaluating your current infrastructure.'
                },
                {
                    'title': 'Planning',
                    'description': 'Designing cloud architecture.'
                },
                {
                    'title': 'Migration',
                    'description': 'Implementing cloud solutions.'
                },
                {
                    'title': 'Optimization',
                    'description': 'Continuous monitoring and improvement.'
                }
            ]
        },
        'ui-ux-design': {
            'id': 'ui-ux-design',
            'title': 'UI/UX Design',
            'description': 'Create beautiful and intuitive user experiences.',
            'icon': 'fas fa-paint-brush',
            'features': [
                {
                    'title': 'User Research',
                    'description': 'Understanding your users\' needs and behaviors.'
                },
                {
                    'title': 'Interface Design',
                    'description': 'Creating visually appealing designs.'
                },
                {
                    'title': 'Prototyping',
                    'description': 'Interactive prototypes for testing.'
                },
                {
                    'title': 'Design Systems',
                    'description': 'Consistent design language and components.'
                }
            ],
            'pricing_plans': [
                {
                    'name': 'Basic',
                    'price': '1499',
                    'period': 'project',
                    'features': [
                        'Basic Research',
                        'UI Design',
                        'Basic Prototype',
                        '1 Revision'
                    ]
                },
                {
                    'name': 'Professional',
                    'price': '2999',
                    'period': 'project',
                    'recommended': True,
                    'features': [
                        'Full Research',
                        'UI/UX Design',
                        'Interactive Prototype',
                        '3 Revisions'
                    ]
                },
                {
                    'name': 'Enterprise',
                    'price': '4999',
                    'period': 'project',
                    'features': [
                        'Advanced Research',
                        'Design System',
                        'Multiple Prototypes',
                        'Unlimited Revisions'
                    ]
                }
            ],
            'process_steps': [
                {
                    'title': 'Research',
                    'description': 'Understanding users and competitors.'
                },
                {
                    'title': 'Wireframing',
                    'description': 'Creating layout and structure.'
                },
                {
                    'title': 'Design',
                    'description': 'Developing visual design and interactions.'
                },
                {
                    'title': 'Testing',
                    'description': 'User testing and refinement.'
                }
            ]
        },
        'ai-robotics': {
            'id': 'ai-robotics',
            'title': 'AI & Robotics',
            'description': 'Harness the power of artificial intelligence and robotics for your business.',
            'icon': 'fas fa-robot',
            'features': [
                {
                    'title': 'AI Consulting',
                    'description': 'Expert guidance on AI adoption and strategy.'
                },
                {
                    'title': 'Machine Learning',
                    'description': 'Building predictive models and intelligent systems.'
                },
                {
                    'title': 'Robotics Development',
                    'description': 'Designing and building custom robotic systems.'
                },
                {
                    'title': 'Computer Vision',
                    'description': 'Image and video analysis for automation and insights.'
                }
            ],
            'pricing_plans': [
                {
                    'name': 'Basic',
                    'price': '1999',
                    'period': 'project',
                    'features': [
                        'Basic AI Consulting',
                        'Machine Learning',
                        'Basic Robotics',
                        '1 Month Support'
                    ]
                },
                {
                    'name': 'Professional',
                    'price': '3999',
                    'period': 'project',
                    'recommended': True,
                    'features': [
                        'Advanced AI Consulting',
                        'Custom Machine Learning',
                        'Advanced Robotics',
                        '3 Months Support'
                    ]
                },
                {
                    'name': 'Enterprise',
                    'price': '6999',
                    'period': 'project',
                    'features': [
                        'Custom AI Solutions',
                        'Dedicated Support',
                        'Custom Robotics',
                        '6 Months Support'
                    ]
                }
            ],
            'process_steps': [
                {
                    'title': 'Discovery',
                    'description': 'Understanding your AI and robotics needs.'
                },
                {
                    'title': 'Strategy',
                    'description': 'Developing a customized AI and robotics plan.'
                },
                {
                    'title': 'Development',
                    'description': 'Building and testing your AI and robotics solutions.'
                },
                {
                    'title': 'Deployment',
                    'description': 'Implementing and integrating your AI and robotics solutions.'
                }
            ]
        }
    }
    
    service = services_data.get(service_id)
    if not service:
        messages.error(request, 'Service not found.')
        return redirect('home')
    
    return render(request, 'core/service_detail.html', {'service': service})

def book_service(request, service_id):
    if request.method == 'POST':
        service = next((s for s in services_data.values() if s['id'] == service_id), None)
        if not service:
            messages.error(request, 'Service not found.')
            return redirect('home')

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        preferred_date = request.POST.get('preferred_date')
        plan_name = request.POST.get('plan_name')

        # Send email notification
        subject = f'New Booking Request: {service["title"]} - {plan_name}'
        email_message = f"""
        New booking request details:
        
        Service: {service["title"]}
        Plan: {plan_name}
        Name: {name}
        Email: {email}
        Phone: {phone}
        Preferred Date: {preferred_date}
        
        Message:
        {message}
        """
        
        try:
            send_mail(
                subject,
                email_message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.ADMIN_EMAIL],
                fail_silently=False,
            )
            messages.success(request, 'Your booking request has been submitted successfully. We will contact you soon.')
        except Exception as e:
            messages.error(request, 'There was an error submitting your booking. Please try again later.')
        
        return redirect('service_detail', service_id=service_id)
    
    return redirect('service_detail', service_id=service_id)
