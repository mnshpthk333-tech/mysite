from datetime import date

from django.shortcuts import render
from django.template.loader import render_to_string

from django.http import Http404, HttpResponseNotFound

# Create your views here.

all_posts=[
    {
        "slug":"travel-to-udaipur",
        "image": "udaipur.jpeg",
        "author":"Manisha",
        "date": date(2026, 1, 12),
        "title": "Udaipur_diaries",
        "excerpt":"Udaipur, the City of Lakes, is a perfect blend of royal heritage and natural beauty. Its grand palaces and peaceful lakes create a romantic and timeless travel experience.",
        "content":"""Udaipur, known as the City of Lakes, is one of the most charming cities in Rajasthan. Surrounded by the Aravalli Hills, the city offers a perfect mix of history, culture, and natural beauty. My journey to Udaipur felt like stepping into a royal story.

The City Palace and Lake Pichola were the highlights of the trip. A boat ride on Lake Pichola during sunset was peaceful and unforgettable. The old streets, local markets, and traditional Rajasthani food added color and flavor to the experience.

Udaipur is a perfect destination for travelers who enjoy calm surroundings, historical places, and cultural richness. It is a city that leaves lasting memories and a desire to visit again.
"""
    },
{
        "slug":"hike-in-the-mountains",
        "image": "VOF.jpeg",
        "author":"Manisha",
        "date": date(2026, 1, 12),
        "title": "Valley of flower diaries",
        "excerpt":"The Valley of Flowers is a breathtaking Himalayan paradise filled with vibrant blooms and fresh mountain air. It offers a peaceful escape into untouched natural beauty.",
        "content":"""The Valley of Flowers, located in Uttarakhand, is a beautiful national park known for its colorful alpine flowers and scenic landscapes. Nestled in the Himalayas, this valley blooms with hundreds of rare flowers during the monsoon season, creating a natural carpet of colors.

The trek to the Valley of Flowers is peaceful and refreshing, surrounded by snow-covered mountains, rivers, and fresh air. The place is also home to diverse wildlife and is a UNESCO World Heritage Site.

With its natural beauty and calm atmosphere, the Valley of Flowers is a perfect destination for nature lovers and trekkers."""
    },
{
        "slug":"travel-to-goa",
        "image": "Goa.jpeg",
        "author":"Manisha",
        "date": date(2026, 1, 12),
        "title": "Goa Diaries",
        "excerpt":"Goa is a lively coastal destination known for its golden beaches, relaxed vibe, and cultural charm. It is the perfect place to enjoy sunsets, sea breeze, and joyful moments.",
        "content":"""Goa is one of the most popular travel destinations in India, known for its beautiful beaches, vibrant nightlife, and relaxed lifestyle. Located on the western coast, Goa offers a unique blend of Indian and Portuguese culture.

The golden beaches like Baga, Calangute, and Anjuna are ideal for relaxation and water sports. Goa is also famous for its old churches, local markets, and delicious seafood. The peaceful sunsets and lively atmosphere make every moment special.

Goa is a perfect place for travelers who want fun, adventure, and calmness all in one destination.
        """
    },
{
        "slug":"travel-to-jaipur",
        "image": "Mountain.jpeg",
        "author":"Manisha",
        "date": date(2026, 1, 12),
        "title": "Jaipur Diaries",
        "excerpt":"Jaipur, the Pink City of India, reflects royal grandeur through its forts, palaces, and colorful streets. Its rich history and vibrant culture make it a must-visit destination.",
        "content":"""Jaipur, the capital of Rajasthan, is known as the Pink City because of its beautiful pink-colored buildings. Founded by Maharaja Sawai Jai Singh II, the city is famous for its rich history, royal palaces, and grand forts.

Popular attractions like Hawa Mahal, City Palace, and Amber Fort reflect Jaipur’s architectural beauty. The city is also known for its colorful markets, traditional handicrafts, and delicious Rajasthani food.

With its royal heritage and vibrant culture, Jaipur is one of the most fascinating tourist destinations in India.
        """
    },

{
        "slug":"travel-to-Nainital",
        "image": "nainital.jpeg",
        "author":"Manisha",
        "date": date(2026, 1, 12),
        "title": "Nainital Diaries",
        "excerpt":"Nainital is a peaceful hill station known for its beautiful lake, cool climate, and scenic mountain views.",
        "content":"""Nainital is a beautiful hill station in Uttarakhand, famous for its scenic lakes and pleasant weather. Surrounded by green hills, the town is built around the peaceful Naini Lake, which is the main attraction for visitors. Boating on the lake and walking along the Mall Road are popular activities.

Nainital also offers stunning viewpoints like Snow View Point and Tiffin Top, which provide breathtaking views of the Himalayas. With its calm environment and natural beauty, Nainital is an ideal destination for nature lovers and families."""
    },

{
        "slug":"travel-to-Rishikesh",
        "image": "Rishikesh.jpeg",
        "author":"Manisha",
        "date": date(2026, 1, 12),
        "title": "Rishikesh Diaries",
        "excerpt":"Rishikesh is a spiritual town where yoga, adventure, and the sacred Ganga come together in harmony.",
        "content":"""Rishikesh, located on the banks of the holy River Ganga, is a spiritual and adventure destination in Uttarakhand. Known as the Yoga Capital of the World, the city attracts visitors from all over the globe for meditation, yoga, and peace.

Apart from spirituality, Rishikesh is also famous for adventure sports like river rafting, bungee jumping, and trekking. The evening Ganga Aarti at Triveni Ghat creates a calm and divine atmosphere, making Rishikesh a unique travel experience."""
    }

]

def get_date(post):
    return post['date']

def starting_page(request):
    sorted_post=sorted(all_posts, key=get_date)
    latest_post=sorted_post[-3:]
    return render(request, "blog/index.html", {
            "posts":latest_post})
    

def posts(request):
    return render(request, "blog/all-post.html", {
        "all_posts":all_posts
    })

def post_details(request, slug):
    identified_post=next(post for post in all_posts if post["slug"]==slug)
    return render(request, 'blog/post-detail.html',{
        "post":identified_post
        })

        