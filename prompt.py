from openai import OpenAI

SYSTEM_PROMPT = """
  Use the provided song title, artist, and lyrics to generate a descriptive prompt that can be used to create a visual representation of the song.
  Your prompt should start with the medium (eg "a photo of..", "an acrylic painting of", "a cartoon of", etc), then describe the visuals, subject and setting of the image also include descriptive words indicating style of the image (eg "photorealistic", "cartoonish", "abstract", etc). Invoke the specific artists or schools of art by including their name in the prompt eg "a surreal painting, Salvidor Dali", "impressionist, Monet", "Renaissance, Raphael"
  Use descriptive words and phrases that evoke the emotions and themes of the song.
  When appropriate, include specific details from the lyrics in your prompt.
  You can also use what you know about the artist, song title, or lyrics to include specific styles, eras of art, or artists in your prompt.
  Include only the prompt in your response. Don't mention that the prompt is generated using song lyrics. Only include descriptive words.
  Don't mention themes of the song, and only describe the visuals of the image.
"""

class OpenAIPromptGenerator:
    client = OpenAI()
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "title": ("STRING",),
                "artist": ("STRING",),
                "lyrics": ("STRING",),
            },
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)

    FUNCTION = "run"

    CATEGORY = "Synesthesia"

    def run(self, title, artist, lyrics):
        completion = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "system",
                "content": SYSTEM_PROMPT
            }, {
                "role": "user",
                "content": f"{title} by {artist} lyrics: {lyrics}"
            }],
            temperature=0.9,
            stream=False,
        )

        return (completion.choices[0].message.content,)
