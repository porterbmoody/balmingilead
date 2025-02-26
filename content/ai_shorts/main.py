from text_llm import TextLLM
from voice_llm import VoiceLLM
from image_llm import ImageLLM
from combiner import Combiner

def main():
    # Get user input
    prompt = input("Enter your YouTube Shorts topic: ")
    
    # Initialize components
    text_llm = TextLLM()
    voice_llm = VoiceLLM()
    image_llm = ImageLLM()
    combiner = Combiner()
    
    # Generate script
    print("Generating script...")
    script = text_llm.get_script(prompt)
    
    # Generate audio
    print("Converting script to speech...")
    audio = voice_llm.get_text_to_speech(script)
    
    # Generate image prompts
    print("Creating image prompts...")
    image_prompts = text_llm.get_image_prompts(audio.transcript, audio.timestamps)
    
    # Generate images
    print("Generating images...")
    images = image_llm.get_images(image_prompts)
    
    # Create image clips
    print("Creating image clips with effects...")
    image_clips = combiner.create_image_clips(images, image_prompts)
    
    # Get background music
    print("Selecting background music...")
    music = combiner.get_background_music(audio.timestamps)
    
    # Combine everything
    print("Combining all elements into final video...")
    final_video = combiner.combine_all_videos(
        image_clips, 
        audio.timestamps, 
        audio.transcript, 
        music
    )
    
    print(f"Video generated successfully! Saved to: {final_video}")

if __name__ == "__main__":
    main() 