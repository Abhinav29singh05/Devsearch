from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .models import Project,Tag
from .forms import ProjectForm, ReviewForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage 
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .utils import searchProjects,paginateProjects


# projectsList = [
#     {
#         'id': '1',
#         'title': "Ecommerce Website",
#         'description': 'Fully functional ecommerce website',
#     },
#     {
#         'id': '2',
#         'title': "Portfolio Website",
#         'description': 'This was a project where I built out my portfolio',
#     },
#     {
#         'id': '3',
#         'title': "Social Network",
#         'description': 'Awesome open source project I am still working on',
#     },
# ]

def projects(request):
    projects,search_query=searchProjects(request)
    
    custom_range,projects=paginateProjects(request,projects,9)

    context={'projects':projects ,'search_query':search_query, 'custom_range':custom_range}
    return render(request,'projects/projects.html',context,)

def project(request,pk):
    projectObj=Project.objects.get(id=pk)
    # tags=projectObj.tags.all() //to use directly in sinle project
    form=ReviewForm()

    if request.method=='POST':
        form=ReviewForm(request.POST)
        review=form.save(commit=False)
        review.project=projectObj
        review.owner=request.user.profile
        review.save()
        projectObj.getVoteCount
        messages.success(request,'Review Successfullt submitted')
        return redirect('project', pk=projectObj.id)

        


    return render(request,'projects/single-project.html',{'project':projectObj, 'form':form})


@login_required(login_url="login")
def createProject(request):
    profile=request.user.profile
    form=ProjectForm()
    if request.method=='POST':
        newTags=request.POST.get('newtags', '').replace(','," ").split()
        form=ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                project=form.save(commit=False)
                project.owner=profile
                project.save()
                
                for tag in newTags:
                    if tag.strip():  # Only add non-empty tags
                        tag_obj, created=Tag.objects.get_or_create(name=tag.strip())
                        project.tags.add(tag_obj)

                messages.success(request, 'Project created successfully!')
                return redirect('account')
            except Exception as e:
                messages.error(request, f'Error creating project: {str(e)}')
        else:
            messages.error(request, 'Please correct the errors below.')
        
    context={'form':form}
    return render(request,"projects/project_form.html",context)


@login_required(login_url="login")
def updateProject(request,pk):
    profile=request.user.profile
    project=profile.project_set.get(id=pk)
    form=ProjectForm(instance=project)
    if request.method=='POST':
        newTags=request.POST.get('newtags').replace(','," ").split()
        form=ProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            project=form.save()
            for tag in newTags:
                tag,created=Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            return redirect('account')
         
    context={'form':form,'project':project}
    return render(request,"projects/project_form.html",context)



@login_required(login_url="login")
def deleteProject(request,pk):
    profile=request.user.profile
    project=profile.project_set.get(id=pk)
    if request.method=='POST':
        project.delete()
        return redirect('account')
     
    context={'object':project}
    return render(request,'delete_template.html',context)

