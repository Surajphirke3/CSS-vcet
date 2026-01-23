import pandas as pd

# Load CSV
df = pd.read_csv("analysis.csv")

print("Welcome to Python Tools Q&A!")
print("Type 'exit' to quit.\n")

while True:
    question = input("You: ").lower()

    if question == "exit":
        print("Goodbye 👋")
        break

    # Look for keywords in question
    found = False
    for index, row in df.iterrows():
        if "pycharm" in question and "pycharm" in row['Tool'].lower():
            found = True
            if "best for" in question:
                print("AI:", row['Best_For'])
            elif "pros" in question:
                print("AI:", row['Pros'])
            elif "cons" in question:
                print("AI:", row['Cons'])
            elif "type" in question:
                print("AI:", row['Type'])
            elif "primary use" in question or "use" in question:
                print("AI:", row['Primary_Use'])
            else:
                print(
                    "AI: I can tell you about Type, Primary Use, Pros, Cons, Best For, File Types, Visualization, Installation")

        elif "jupyter" in question and "jupyter" in row['Tool'].lower():
            found = True
            if "best for" in question:
                print("AI:", row['Best_For'])
            elif "pros" in question:
                print("AI:", row['Pros'])
            elif "cons" in question:
                print("AI:", row['Cons'])
            elif "type" in question:
                print("AI:", row['Type'])
            elif "primary use" in question or "use" in question:
                print("AI:", row['Primary_Use'])
            else:
                print(
                    "AI: I can tell you about Type, Primary Use, Pros, Cons, Best For, File Types, Visualization, Installation")

        elif "anaconda" in question and "anaconda" in row['Tool'].lower():
            found = True
            if "best for" in question:
                print("AI:", row['Best_For'])
            elif "pros" in question:
                print("AI:", row['Pros'])
            elif "cons" in question:
                print("AI:", row['Cons'])
            elif "type" in question:
                print("AI:", row['Type'])
            elif "primary use" in question or "use" in question:
                print("AI:", row['Primary_Use'])
            else:
                print(
                    "AI: I can tell you about Type, Primary Use, Pros, Cons, Best For, File Types, Visualization, Installation")

    if not found:
        print("AI: Sorry, I don't have information on that. Try PyCharm, Jupyter, or Anaconda.")
