from django.shortcuts import render, redirect

from exam_prep_one.albums.forms import AlbumCreateForm, AlbumEditForm, AlbumDeleteForm
from exam_prep_one.albums.models import Album
from exam_prep_one.mainpage.views import get_profile


def album_add(request):
    # album_create_form = AlbumCreateForm(request.POST or None)
    # if request.method == 'POST':
    #     if album_create_form.is_valid():
    #         created_album = album_create_form.save()
    #         return redirect('album_details', pk=created_album.pk)
    #
    if request.method == 'POST':
        album_create_form = AlbumCreateForm(request.POST)
        if album_create_form.is_valid():
            instance = album_create_form.save(commit=False)
            instance.owner = get_profile()
            instance.save()
            return redirect('index')
            # return redirect('album_details', pk=instance.pk)
    else:
        album_create_form = AlbumCreateForm()

    context = {
        'album_create_form': album_create_form,
    }
    return render(request, 'albums/album-add.html', context)


def album_details(request, pk):
    context = {
        'album': Album.objects.get(pk=pk)
    }
    return render(request, 'albums/album-details.html', context)


def album_edit(request, pk):
    album = Album.objects.filter(pk=pk).get()
    album_edit_form = AlbumEditForm(request.POST or None, instance=album)

    if request.method == 'POST':
        if album_edit_form.is_valid():
            album_edit_form.save()
            return redirect('album_details', pk=album.pk)

    context = {
        'album_edit_form': album_edit_form,
        'album': album,
    }
    return render(request, 'albums/album-edit.html', context)


def album_delete(request, pk):
    album = Album.objects.get(pk=pk)

    album_delete_form = AlbumDeleteForm(request.POST or None, instance=album)

    if request.method == 'POST':
        album_delete_form.save()
        return redirect('index')

    context = {
        'album': album,
        'album_delete_form': album_delete_form,
        'pk': pk,
    }

    return render(request, 'albums/album-delete.html', context)
