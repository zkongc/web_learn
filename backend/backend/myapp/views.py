from django.http import JsonResponse

# 模拟视频数据
# videos = [
#     { "id": "video1", "title": "视频 1：React基础教程", "bvid": "BV1ff4y1P7G2" },
#     { "id": "video2", "title": "视频 2：Vue3 基础教程", "bvid": "BV1mUqGYEE8v" },
#     { "id": "video3", "title": "视频 3：春节", "bvid": "BV14TFTeHEFP" }
# ]
videos = [
    { "id": 1, "title": "React基础教程", "bvid": "BV1ff4y1P7G2" },
    { "id": 2, "title": "Vue3 基础教程", "bvid": "BV1mUqGYEE8v" },
    { "id": 3, "title": "春节", "bvid": "BV14TFTeHEFP" },
    { "id": 4, "title": "春节", "bvid": "BV14TFTeHEFP" },
    { "id": 5, "title": "春节", "bvid": "BV14TFTeHEFP" },
    { "id": 6, "title": "春节", "bvid": "BV14TFTeHEFP" },
    { "id": 7, "title": "春节", "bvid": "BV14TFTeHEFP" },
    { "id": 8, "title": "春节", "bvid": "BV14TFTeHEFP" },
    { "id": 9, "title": "春节", "bvid": "BV14TFTeHEFP" },
    { "id": 10, "title": "xx", "bvid": "BV14TFTeHEFP" }
]


# API视图返回视频数据
def video_list(request):
    return JsonResponse(videos, safe=False)
