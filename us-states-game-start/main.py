import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="whats another states name").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        # missing_state = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_state.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

screen.exitonclick()

# data_row = data[data.state == answer_state]
# print(data_row.x, data_row.y)
# text = turtle
#
# Font = ('Arial', 7, 'normal')
#
#
# def my_text(answer, x, y):
#     turtle.penup()
#     turtle.write(answer, font=Font)
#     turtle.goto(x, y)
#
#
# my_text(answer=answer_state, x=int(data_row.x), y=int(data_row.y))
