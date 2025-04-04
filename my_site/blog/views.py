from datetime import date

from django.shortcuts import render

from .models import Post

all_posts = [
    # {
    #     "slug": "hike-in-the-mountains",
    #     "image": "mountains.jpg",
    #     "author": "Ana Md",
    #     "date": date(2021, 7, 21),
    #     "title": "Mountain Hiking",
    #     "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
    #     "content": """
    #       Hiking in the mountains offers a breathtaking experience, with stunning landscapes and fresh air that refreshes the mind and body. 
    #       On my latest hike, I found myself surrounded by towering peaks and lush green valleys, the perfect escape from daily life.

    #       As I reached the summit, the view was unlike anything I had ever seen before—a vast expanse of rolling hills, distant rivers, and 
    #       the golden glow of the setting sun. Just as I was soaking in the beauty, a sudden movement in the bushes caught my attention. 
    #       A family of deer gracefully crossed my path, reminding me of nature’s wonders.

    #       The journey down was just as thrilling, with rocky paths testing my endurance and a cool mountain breeze offering comfort. 
    #       Every step was a reminder that adventure awaits those who seek it.
    #     """
    # },
    # {
    #     "slug": "programming-is-fun",
    #     "image": "coding.jpg",
    #     "author": "Ana Md",
    #     "date": date(2022, 3, 10),
    #     "title": "Programming Is Great!",
    #     "excerpt": "Did you ever spend hours searching for that one error in your code? Yep - that's what happened to me yesterday...",
    #     "content": """
    #       Programming is both an art and a science. It requires creativity, problem-solving skills, and patience. 
    #       Yesterday, I spent hours debugging a tricky piece of code, only to realize that a single missing semicolon was the culprit!

    #       Despite the challenges, coding offers a deep sense of satisfaction. Building something from scratch, whether it’s a simple 
    #       calculator or a complex web application, gives a sense of accomplishment like no other. The ability to bring ideas to life 
    #       through code is what keeps me coming back.

    #       Every error teaches a lesson, and every successful execution is a victory. That’s why programming is more than just work—it’s 
    #       an exciting journey of learning and innovation.
    #     """
    # },
    # {
    #     "slug": "into-the-woods",
    #     "image": "woods.jpg",
    #     "author": "Ana Md",
    #     "date": date(2020, 8, 5),
    #     "title": "Nature At Its Best",
    #     "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
    #     "content": """
    #       Walking into the woods feels like stepping into another world. The towering trees, chirping birds, and the rustling leaves 
    #       create a sense of calm and peace that is hard to find in the busy city.

    #       As I wandered deeper, I discovered a hidden stream, its clear water reflecting the sunlight. The air was fresh, and the scent of 
    #       pine and earth filled my lungs. It’s moments like these that remind me why nature is the ultimate retreat.

    #       Spending time in the woods is more than just a walk—it’s a chance to reconnect with ourselves, clear our minds, and appreciate 
    #       the beauty that surrounds us. In nature, we find inspiration, tranquility, and the motivation to keep moving forward.
    #     """
    # },
    # {
    #     "slug": "tech-trends-2025",
    #     "image": "tech.jpg",
    #     "author": "Ana Mohammed",
    #     "date": date(2025, 2, 15),
    #     "title": "The Future of Tech: Trends to Watch",
    #     "excerpt": "Technology is evolving at an unprecedented pace. Let's explore some key trends shaping the future!",
    #     "content": """  
    #       From AI-driven automation to quantum computing, the world of technology is advancing rapidly.  
    #       We explore the most exciting innovations and what they mean for businesses and consumers.  
    #       Stay ahead of the curve and discover what the future holds!
    #     """
    # },
    # {
    #     "slug": "deep-work-productivity",
    #     "image": "deep-work.jpg",
    #     "author": "Ana Mohammed",
    #     "date": date(2024, 11, 8),
    #     "title": "Mastering Deep Work for Maximum Productivity",
    #     "excerpt": "Struggling with distractions? Learn how to get into deep work mode and boost your productivity.",
    #     "content": """  
    #       In a world filled with distractions, mastering deep work is the key to achieving high-impact results.  
    #       This article covers proven strategies to help you enter deep focus mode, avoid distractions,  
    #       and produce high-quality work efficiently.
    #     """
    # },
    # {
    #     "slug": "ai-in-web-development",
    #     "image": "ai-web.jpg",
    #     "author": "Ana Mohammed",
    #     "date": date(2024, 6, 25),
    #     "title": "How AI is Changing Web Development",
    #     "excerpt": "AI tools are revolutionizing web development. Should you embrace them or stick to traditional methods?",
    #     "content": """  
    #       With AI-driven code generators, design assistants, and automation tools,  
    #       web development is undergoing a transformation. We discuss the advantages, limitations,  
    #       and best practices for leveraging AI in modern development workflows.
    #     """
    # },
]

def get_date(post):
    return post['date']

# Create your views here.


def starting_page(request):
    latest_posts = Post.objects.all().order_by('-date')[:3]
    # sorted_posts = sorted(all_posts, key=get_date)
    # latest_posts = sorted_posts[-3:]  # Show the latest 3 posts
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })