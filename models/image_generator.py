def generate_image(context):
    topic = context['topic']
    emotion = context['emotion']
    action = context['action']

    # Dummy image generation logic
    image_url = f"https://via.placeholder.com/300x200.png?text={topic}_{emotion}_{action}"
    return image_url