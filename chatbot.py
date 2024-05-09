import random

# Define responses for different inputs
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "hello": ["Hi!", "Hello!", "Hey there!"],
    "how are you": ["I'm doing well, thank you!", "I'm fine, thanks for asking.", "I'm good, how about you?"],
    "i'm good too": ['Thats good to know', "Thats great!"],
    "what's your name": ["I'm a chatbot!", "You can call me Chatbot.", "I'm your friendly chatbot!"],
    "bye": ["Goodbye!", "Bye!", "See you later!"],
    "thank you": ["You're welcome!", "No problem!", "Anytime!"],
    "can you help me": ["Sure! whats up", "Definitely", "Yeah go on"],
    "i need a book recommendation": ["Do u have any specific genre in my mind?"],
    "no i dont": ["No worries. How about a Mystery Thriller or a Romance or a Science Fiction or a Fantasy or a Adventure or a Historical Fiction or a Young Adult (YA) or a Non-fiction or a Horror or a Biography/Autobiography?"],
    "mystery thriller": ["Sure! You can read - The Woman in White by Wilkie Collins, A Good Girl's Guide to Murder by Holly Jackson, The Mindf*ck series by S.T. Abby, The Murder of Roger Ackroyd by Agatha Christie, Rebecca by Daphne du Maurier, The Shining by Stephen King, The Silence of the Lambs by Thomas Harris, Gone Girl by Gillian Flynn, The Shadow of the Wind by Carlos Ruiz Zafón, The Girl With The Dragon Tattoo by Stieg Larsson"],
    "romance": ["Sure! You can read - The Hating Game by Sally Thorne, Happily Ever After by Lynn Painter, Girl Abroad by Elle Kennedy, The Kiss Quotient by Helen Hoang, Fangirl Down by tessa Bailey, Better Than The Movies by Lynn Painter, I Hope This Doesn't Find You by Ann Liang, The Wicked King by Holly Black, People We Meet On Vacation by Emily Henry, Red,White & Blue by Cassy McQuiston"],
    "science fiction": ["Sure! You can read- Dune by Frank Herbert, Neuromancer by William Gibson, The Hitchhiker's Guide to the Galaxy by Douglas Adams, Ender's Game by Orson Scott Card, Snow Crash by Neal Stephenson, Foundation by Isaac Asimov, Hyperion by Dan Simmons, The Left Hand of Darkness by Ursula K. Le Guin, The Martian by Andy Weir, The War of the Worlds by H.G. Wells."],
    "fantasy": ["Sure! You can read The Lord of the Rings by J.R.R. Tolkien, Harry Potter series by J.K. Rowling, A Song of Ice and Fire series by George R.R. Martin, The Chronicles of Narnia by C.S. Lewis, Mistborn series by Brandon Sanderson, The Name of the Wind by Patrick Rothfuss, The Wheel of Time series by Robert Jordan, The Dresden Files series by Jim Butcher, His Dark Materials series by Philip Pullman, The Stormlight Archive series by Brandon Sanderson."],
    "adventure": ["Sure! You can read Treasure Island by Robert Louis Stevenson, The Adventures of Huckleberry Finn by Mark Twain, Jurassic Park by Michael Crichton, The Count of Monte Cristo by Alexandre Dumas, The Hobbit by J.R.R. Tolkien, Around the World in Eighty Days by Jules Verne, Robinson Crusoe by Daniel Defoe, Journey to the Center of the Earth by Jules Verne, The Swiss Family Robinson by Johann David Wyss, The Call of the Wild by Jack London."],
    "historical fiction": ["Sure! You can read The Nightingale by Kristin Hannah, All the Light We Cannot See by Anthony Doerr, The Book Thief by Markus Zusak, The Help by Kathryn Stockett, The Pillars of the Earth by Ken Follett, The Underground Railroad by Colson Whitehead, The Kite Runner by Khaled Hosseini, The Tattooist of Auschwitz by Heather Morris, Girl with a Pearl Earring by Tracy Chevalier, The Alice Network by Kate Quinn."],
    "young adult": ["Sure! You can read The Hunger Games by Suzanne Collins, The Fault in Our Stars by John Green, Harry Potter series by J.K. Rowling, To All the Boys I've Loved Before by Jenny Han, The Perks of Being a Wallflower by Stephen Chbosky, The Maze Runner series by James Dashner, Twilight series by Stephenie Meyer, Percy Jackson & the Olympians series by Rick Riordan, The Hate U Give by Angie Thomas, Divergent series by Veronica Roth."],
    "non fiction": ["Sure! You can read The Diary of a Young Girl by Anne Frank, Sapiens: A Brief History of Humankind by Yuval Noah Harari, Educated by Tara Westover, Becoming by Michelle Obama, The Immortal Life of Henrietta Lacks by Rebecca Skloot, Born a Crime: Stories from a South African Childhood by Trevor Noah, Shoe Dog: A Memoir by the Creator of Nike by Phil Knight, The Glass Castle by Jeannette Walls, Just Mercy: A Story of Justice and Redemption by Bryan Stevenson, Hillbilly Elegy: A Memoir of a Family and Culture in Crisis by J.D. Vance."],
    "horror": ["Sure! You can read Dracula by Bram Stoker, The Shining by Stephen King, Frankenstein by Mary Shelley, The Exorcist by William Peter Blatty, Pet Sematary by Stephen King, The Haunting of Hill House by Shirley Jackson, IT by Stephen King, The Silence of the Lambs by Thomas Harris, Interview with the Vampire by Anne Rice, The Turn of the Screw by Henry James."],
    "biography/autobiography": ["Sure! You can read The Autobiography of Malcolm X by Malcolm X and Alex Haley, Steve Jobs by Walter Isaacson, Long Walk to Freedom by Nelson Mandela, Bossypants by Tina Fey, Becoming by Michelle Obama, The Diary of a Young Girl by Anne Frank, Tuesdays with Morrie by Mitch Albom, Night by Elie Wiesel, Angela's Ashes by Frank McCourt, The Glass Castle by Jeannette Walls."]
}

def chatbot_response(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()
    
    # Check if the input matches any predefined responses
    for key in responses:
        if user_input in key:
            return random.choice(responses[key])
    
    # If no predefined response is found, return a default response
    return "I'm not sure how to respond to that."

# Main function to interact with the chatbot
def main():
    print("Welcome to the Chatbot! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print(chatbot_response(user_input))
            break
        else:
            print("Chatbot:", chatbot_response(user_input))

# Run the chatbot
if __name__ == "__main__":
    main()
