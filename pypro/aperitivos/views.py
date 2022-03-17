from django.shortcuts import render


def video(request, slug):
    video = {'titulo': 'Video Aperitivo: Motivação', 'vimeo_id': '688602515?h=a0a828a5ea'}
    return render(request, 'aperitivos/video.html', context={'video': video})
