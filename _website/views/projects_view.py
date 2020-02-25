from _website.views.view import View
from django.shortcuts import render
from _website.models import Request


class ProjectsView(View):
    def get(self, request):
        self.log('ProjectsView.get()')
        from _database.models import Project
        from secrets import Secret

        request = Request(request)

        all_results = Project.objects.all()[:10]
        context = {
            'view': 'projects_view',
            'in_space': request.in_space,
            'hash': request.hash,
            'ADMIN_URL': self.admin_url,
            'user': request.user,
            'language': request.language,
            'auto_search': request.search,
            'slug': '/projects',
            'page_git_url': '/tree/master/_database/templates/results_list.html',
            'page_name': self.space_name+' | Projects',
            'page_description': 'People at '+self.space_name+' created all kinds of awesome projects!',
            'headline': 'Projects',
            'description': 'At {} fellow hackers created awesome projects...'.format(self.space_name),
            'wiki_url': None,
            'add_new_requires_user': False,
            'addnew_url': '{}c/projects/'.format(Secret('DISCOURSE.DISCOURSE_URL').value),
            'addnew_text': 'Add project',
            'all_results': all_results if all_results else True,
            'results_count': Project.objects.count(),
            'show_more': 'projects'
        }

        return render(request.request, 'page.html', context)
