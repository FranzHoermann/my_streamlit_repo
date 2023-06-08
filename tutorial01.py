import streamlit as st
st.title("Streamlit Tutorial App")
st.write("This is my new app")
button1 = st.button("Click Me")
if button1:
	st.write("This is some text.")
	
st.header("Start of the Checkbox Section")
like = st.checkbox("Do you like this app?")
button2 = st.button("Submit")
if button2:
	if like:
		st.write("Tanks. I like it too.")
	else:
		st.write("I'm sorry. You have bad tastes.")
		
st.header("Start of the Radio Button Section")

animal = st.radio("What animal is your favorite?", ("Lions", "Tigers", "Bears"))
button3 = st.button("Submit Animal")

if button3:
	st.write(animal)
	if animal == "Lions":
		st.write("ROAR!")
		
st.header("Start of the Selectbox Section")

animal2 = st.selectbox("What animal is your favorite?", ("Lions", "Tigers", "Bears"))
button4 = st.button("Submit Animal 2")

if button4:
	st.write(animal2)
	if animal2 == "Lions":
		st.write("ROAR!")

st.header("Start of the Multiselect Section")
options = st.multiselect("What animals do you like?", ["Lion", "Tiger", "Bear"])
button5 = st.button("Print Animals")

if button5:
	st.write(options)

st.header("Start of the Slider Section")
epochs_num = st.slider("How many epochs?", 1,100,10)
if st.button("Slider Button"):
	st.write(epochs_num)

st.header("Start of the Text Input Section")
user_text = st.text_input("What's your favorite movie?", "Star Wars Ep. IV")
if st.button("Text Button"):
	st.write(user_text)

user_num = 	st.number_input("What's your Age?")
if st.button("Number Button"):
	st.write(user_num)

def run_sentiment_analysis(txt):
	st.write(f"Analysis Done. {txt}")

txt = st.text_area("Text to analyze:", """Es reden und träumen die Menschen viel
Von bessern künftigen Tagen,
Nach einem glücklichen goldenen Ziel
Sieht man sie rennen und jagen.
Die Welt wird alt und wird wieder jung,
Doch der Mensch hofft immer Verbesserung.

Die Hoffnung führt ihn ins Leben ein,
Sie umflattert den fröhlichen Knaben,
Den Jüngling locket ihr Zauberschein,
Sie wird mit dem Greis nicht begraben,
Denn beschließt er im Grabe den müden Lauf,
Noch am Grabe pflanzt er – die Hoffnung auf.

Es ist kein leerer schmeichelnder Wahn,
Erzeugt im Gehirne des Toren,
Im Herzen kündet es laut sich an:
Zu was Besserm sind wir geboren!
Und was die innere Stimme spricht,
Das täuscht die hoffende Seele nicht.""")

st.write("Sentiment:", run_sentiment_analysis(txt))

