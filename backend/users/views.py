from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ExtendedUser, Team
from events.models import Event
from django.contrib.auth import get_user_model
from django.core.mail import get_connection, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import uuid
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .forms import TeamCreationForm, TeamJoiningForm, EditTeamForm
from django.conf import settings

User = get_user_model()


sendMailID = settings.FROM_EMAIL_USER


def registrationNotCompleted(request):
    user = request.user
    if user.is_authenticated and user.isProfileCompleted is False:
        messages.info(request, 'Complete your registration first.')
        return True
    return False


def isRegistrationFormValid(data):
    requiredFields = ['first_name', 'last_name', 'email', 'college_name', 'phone_no', 'gender', 'city', 'current_year']
    for item in requiredFields:
        if item not in data:
            return False
    return True


@login_required
def user_profile(request):
    if(request.method == "POST"):
        data = request.POST
        if isRegistrationFormValid(data):
            user = request.user
            user.first_name = data['first_name']
            user.last_name = data['last_name']

            extendeduser = ExtendedUser.objects.filter(email=request.user.email).first()
            extendeduser.gender = data['gender']

            extendeduser.contact = data['phone_no']
            phone_no = data['phone_no']
            if phone_no.isdecimal() and len(phone_no) == 10:
                extendeduser.contact = phone_no
            else:
                messages.info(request, 'Enter a valid contact number.')
                return render(request, 'profile.html')
            extendeduser.current_year = data['gender']
            extendeduser.college = data['college_name']
            extendeduser.city = data['city']
            extendeduser.current_year = data['current_year']
            if 'referral_code' in data and data['referral_code'] != '' and extendeduser.isProfileCompleted is False:
                referralCode = data['referral_code']
                if ExtendedUser.objects.filter(invite_referral=referralCode).exists():
                    referredBy = ExtendedUser.objects.filter(invite_referral=referralCode).first()
                    #here
                    extendeduser.referred_by = referredBy.user
                else:
                    messages.info(request, 'Invalid Referral Code.')
                    return render(request, 'profile.html')

            extendeduser.first_name = data['first_name']
            extendeduser.last_name = data['last_name']
            extendeduser.isProfileCompleted = True
            user.save()
            extendeduser.save()
            messages.info(request, 'Your profile has been updated.')
            return redirect('/')

        else:
            messages.info(request, 'Fill all the required fields.')

    return render(request, 'profile.html')


@login_required
def my_events(request):
    user = request.user
    if registrationNotCompleted(request):
        return redirect("/users/profile")
    my_teams = user.teams.all()
    categories = []
    for team in my_teams:
        if team.event.type not in categories:
            categories.append(team.event.type)
    return render(request, 'my_events.html', {"my_teams": my_teams, "categories": categories})


@login_required
def create_team(request, eventid):
    user = request.user
    event = get_object_or_404(Event, pk=eventid)
    if registrationNotCompleted(request):
        return redirect("/users/profile")
    if(request.user.teams.filter(event=event).exists()):
        messages.info(request, 'You have already created a team for this event.')
        return redirect(f'/events/{event.type}/{event.pk}')
    if event.registration_open is False:
        messages.info(request, 'Registration for this event is currently closed.')
        return redirect(f'/events/{event.type}/{event.pk}')
    if request.method == 'POST':
        form = TeamCreationForm(request.POST)
        if form.is_valid():
            # if(Team.objects.filter(name = form.cleaned_data['name']).exists()):
            #     # form.add_error('name', 'Team with this given name is already created.')
            #     pass
            # else:
            team = form.save(commit=False)
            team.id = 'PRO' + str(uuid.uuid4().int)[:6]
            team.leader = request.user
            team.event = event
            team.save()
            team.members.add(request.user)
            team.save()
            request.user.extendeduser.events.add(event)
            message = (f"You have successfully created a team {team.name} for the {event.type} event {event.name}. ")
            isTeamEvent = True
            if team.event.type == "poster_presentation":
                message = (f"You have successfully created a team {team.name} for the Poster Presentation contest. ")
                subject = "Poster presentation registration details"
            else:
                message = (f"You have successfully created a team {team.name} for the {event.type} event {event.name}. ")
                subject = f'{event.name} Registration Details'
            with get_connection(
                username=settings.EMAIL_HOST_USER,
                password=settings.EMAIL_HOST_PASSWORD
            ) as connection:
                html_content = render_to_string("eventRegister_confirmation.html", {'first_name': user.first_name, 'team_id': team.id, 'imgURL': event.image, 'message': message, 'isTeamEvent': isTeamEvent})
                text_content = strip_tags(html_content)
                message = EmailMultiAlternatives(subject=subject, body=text_content, from_email=sendMailID, to=[user.email], connection=connection)
                message.attach_alternative(html_content, "text/html")
                message.mixed_subtype = 'related'
                message.send()
            messages.info(request, f'Team Successfully Created, your teamId is {team.id}, which is also sent to your respective email address.')
            return redirect('/users/my_events')
    else:
        form = TeamCreationForm()
    return render(request, 'create_team.html', {'form': form, 'event': event})


@login_required
def register_indi_event(request, eventid):
    user = request.user
    if registrationNotCompleted(request):
        return redirect("/users/profile")
    event = get_object_or_404(Event, pk=eventid)
    if(request.user.teams.filter(event=event).exists()):
        messages.info(request, 'You have already registered for this Event.')
        return redirect(f'/events/{event.type}/{event.pk}')
    if event.registration_open is False:
        messages.info(request, 'Registration for this event is currently closed.')
        return redirect(f'/events/{event.type}/{event.pk}')

    if event.participation_type != 'individual':
        messages.info(request, 'Invalid Request.')
        return redirect(f'/events/{event.type}/{event.pk}')

    team = Team.objects.create(leader=user, pk='PRO' + str(uuid.uuid4().int)[:6], event=event)
    team.name = f"{user.first_name}_{team.pk}"
    team.members.add(user)
    team.save()
    user.extendeduser.events.add(event)
    if event.type == "talk":
        message = (f"You have successfully registered for the seminar of {event.speaker}.")
        subject = (f"{event.speaker} seminar registration details")
        isTeamEvent = False
        # message = (f"You have successfully registered for this talk by {event.speaker}. Your registration ID is {team.id}.\n\nRegards\nPrometeo'22 Team")
    else:
        if event.type == "workshop":
            message = (f"You have successfully registered for the {event.name} workshop.")
            subject = (f"{event.name} workshop registration details")
        elif event.type == "panel_discussion":
            message = (f"You have successfully registered for the {event.name} panel discussion.")
            subject = (f"{event.name} panel discussion registration details")
        elif event.type == "poster_presentation":
            message = "You have successfully registered for the poster presentation."
            subject = "Poster presentation registration details"
        else:
            message = (f"You have successfully registered for the {event.type} event {event.name}.")
            subject = (f"{event.name} registration details")
        isTeamEvent = False
        # message = (f"You have successfully registered for the {event.type} event {event.name}. Your registration ID is {team.id}.\n\nRegards\nPrometeo'22 Team")
    with get_connection(
        username=settings.EMAIL_HOST_USER,
        password=settings.EMAIL_HOST_PASSWORD
    ) as connection:
        html_content = render_to_string("eventRegister_confirmation.html", {'first_name': user.first_name, 'team_id': team.id, 'imgURL': event.image, 'message': message, 'isTeamEvent': isTeamEvent})
        text_content = strip_tags(html_content)
        message = EmailMultiAlternatives(subject=subject, body=text_content, from_email=sendMailID, to=[user.email], connection=connection)
        message.attach_alternative(html_content, "text/html")
        message.mixed_subtype = 'related'
        message.send()
    messages.info(request, f'You have successfully registered for this event, your Registration ID is {team.id}, which has been sent to your respective email address.')
    return redirect('/users/my_events')


@login_required
def make_ca(request):
    user = request.user
    if registrationNotCompleted(request):
        return redirect("/users/profile")

    extendeduser = ExtendedUser.objects.filter(user=user).first()
    if extendeduser.ambassador is False:
        extendeduser.ambassador = True
        invite_referral = 'CA' + str(uuid.uuid4().int)[:6]
        extendeduser.invite_referral = invite_referral
        extendeduser.save()

        with get_connection(
                username=settings.EMAIL_HOST_USER,
                password=settings.EMAIL_HOST_PASSWORD
        ) as connection:
            html_content = render_to_string("ca_confirmation.html", {'first_name': user.first_name, 'invite_referral': invite_referral})
            text_content = strip_tags(html_content)
            message = EmailMultiAlternatives(subject='Campus Ambassador', body=text_content, from_email=sendMailID, to=[user.email], connection=connection)
            message.attach_alternative(html_content, "text/html")
            message.mixed_subtype = 'related'
            message.send()

        messages.info(request, 'You are now a campus ambassador. Please check you email for referral code.')
        return redirect('/')

    else:
        messages.info(request, 'Your are already campus ambassador')
        return redirect('/')


@login_required
def ca_dashboard(request):
    user = request.user
    if registrationNotCompleted(request):
        return redirect("/users/profile")

    extendeduser = ExtendedUser.objects.filter(user=user).first()
    if extendeduser.ambassador is True:
        referral_id = extendeduser.invite_referral
        referred_users = ExtendedUser.objects.filter(referred_by=user)
        count = len(referred_users)
        return render(request, 'dashboard/ca_dashboard.html', {'referral_id': referral_id, 'referred_users': referred_users, 'count': count})
    else:
        messages.info(request, 'Your are not a campus ambassador')
        return redirect('/')


@login_required
def join_team(request):
    if registrationNotCompleted(request):
        return redirect("/users/profile")
    if request.method == 'POST':
        user = request.user
        form = TeamJoiningForm(request.POST)
        if form.is_valid():
            teamId = form.cleaned_data['teamId']
            if(Team.objects.filter(pk=teamId).exists()):
                team = Team.objects.get(pk=teamId)
                if team.event.registration_open is False:
                    messages.info(request, 'Registration for this event is currently closed.')
                    return redirect(f'/events/{team.event.type}/{team.event.pk}')
                if team.event.participation_type != 'team':
                    messages.info(request, 'Only single person is allowed in this event.')
                    return redirect(f'/events/{team.event.type}/{team.event.pk}')
                if request.user in team.members.all():
                    form.add_error(None, 'You are already a member of this team')
                elif team.event in request.user.extendeduser.events.all():
                    form.add_error(None, 'You have already registered for the event ' + team.event.name + ' from a different team')
                elif (team.members.all().count() >= team.event.max_team_size):
                    form.add_error(None, 'Team is already full')
                else:
                    team.members.add(request.user)
                    team.save()
                    request.user.extendeduser.events.add(team.event)
                    isTeamEvent = True
                    if team.event.type == "poster_presentation":
                        message = (f"You have successfully joined the team {team.name} for the Poster Presentation contest. ")
                        subject = "Poster presentation registration details"
                    else:
                        message = (f"You have successfully joined the team {team.name} for the {team.event.type} event {team.event.name}. ")
                        subject = f'{team.event.name} Registration Details'
                    with get_connection(
                        username=settings.EMAIL_HOST_USER,
                        password=settings.EMAIL_HOST_PASSWORD
                    ) as connection:
                        html_content = render_to_string("eventRegister_confirmation.html", {'first_name': user.first_name, 'team_id': team.id, 'imgURL': team.event.image, 'message': message, 'isTeamEvent': isTeamEvent})
                        text_content = strip_tags(html_content)
                        message = EmailMultiAlternatives(subject=subject, body=text_content, from_email=sendMailID, to=[user.email], connection=connection)
                        message.attach_alternative(html_content, "text/html")
                        message.mixed_subtype = 'related'
                        message.send()
                    messages.success(request, f"Successfully joined team '{team.name}'.")
                    return redirect(f'/events/{team.event.type}/{team.event.pk}')

            else:
                form.add_error('teamId', 'No team with the given team ID exists')
    else:
        form = TeamJoiningForm()
    return render(request, 'join_team.html', {'form': form})


@login_required
def edit_team(request, teamid):
    if registrationNotCompleted(request):
        return redirect("/users/profile")
    team = get_object_or_404(Team, id=teamid)
    if(request.user != team.leader):
        messages.info(request, "Only the team leader (creator) can edit the team details.")
        return redirect(f'/events/{team.event.type}/{team.event.pk}')
    elif(team.event.participation_type != 'team'):
        messages.info(request, "Individual Participation event cannot be edited.")
        return redirect(f'/events/{team.event.type}/{team.event.pk}')
    elif(request.method == 'POST'):
        form = EditTeamForm(team, request.POST, instance=team)
        if(form.is_valid()):
            if(team.leader not in form.cleaned_data['members']):
                form.add_error('members', 'You cannot remove the leader (creator) of the team from the team.')
            else:
                for member in team.members.all():
                    if member not in form.cleaned_data['members']:
                        member.extendeduser.events.remove(team.event)
                form.save()
                messages.success(request, "The team details have been updated.")
                return redirect((f'/events/{team.event.type}/{team.event.pk}'))
    else:
        form = EditTeamForm(team, instance=team)
    return render(request, 'edit_team.html', {'form': form, 'team': team})


@login_required
def delete_team(request, teamid):
    if registrationNotCompleted(request):
        return redirect("/users/profile")
    team = get_object_or_404(Team, id=teamid)
    if(request.user != team.leader):
        messages.info(request, "Only the team leader (creator) can delete the team.")
        return redirect(f'/events/{team.event.type}/{team.event.pk}')
    if(team.event.participation_type != 'team'):
        messages.info(request, "Individual Participation cannot be deleted.")
        return redirect(f'/events/{team.event.type}/{team.event.pk}')
    for member in team.members.all():
        member.extendeduser.events.remove(team.event)
    team.delete()
    messages.success(request, f"Successfully deleted team '{team.name}'.")
    return redirect(f'/events/{team.event.type}/{team.event.pk}')
