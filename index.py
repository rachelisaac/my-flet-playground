import flet
import random
from flet import Page, Text, TextField, ElevatedButton, Column, Colors


def main(page: Page):
    page.title = "משחק ניחוש המספר הסודי"
    page.bgcolor = Colors.LIGHT_BLUE  # צבע רקע לחלון

    # פונקציה שמתחילה משחק חדש
    def start_new_game(event=None):
        nonlocal secret_number, guess_count
        secret_number = random.randint(0, 100)
        guess_count = 0
        feedback_text.value = "🎯נסה לנחש את המספר הסודי! (בין 0 ל-100)"
        feedback_text.color = Colors.BLACK
        input_field.value = ""
        if play_again_button in page.controls:
            page.controls.remove(play_again_button)
        page.update()

    # פונקציה לבדיקה של הניחוש
    def check_guess(event):
        nonlocal guess_count
        guess_count += 1
        try:
            guess = int(input_field.value)
        except ValueError:
            feedback_text.value = "הי! הכנס מספר תקין:)"
            feedback_text.color = Colors.RED
            page.update()
            return

        if guess < secret_number:
            feedback_text.value = "⬆️המספר הסודי גדול יותר מהמספר שניחשת"
            feedback_text.color = Colors.BLACK
        elif guess > secret_number:
            feedback_text.value = "⬇️המספר הסודי קטן יותר מהמספר שניחשת"
            feedback_text.color = Colors.ORANGE
        else:
            feedback_text.value = f"🎉 כל הכבוד! ניחשת נכון! המספר היה {secret_number} אחרי {guess_count} ניחושים 👏 ."
            feedback_text.color = Colors.GREEN
            guess_button.visible = False
            page.update()
            page.add(play_again_button)

        input_field.value = ""
        page.update()

    # משתנים ראשוניים
    secret_number = random.randint(0, 100)
    guess_count = 0

    # רכיבים
    feedback_text = Text("נחש מספר בין 0 ל-100", size=24, weight="bold")
    input_field = TextField(label="נחש את המספר הסודי", width=200)
    guess_button = ElevatedButton("🤔נחש ", on_click=check_guess, bgcolor=Colors.BLUE, color=Colors.WHITE)
    play_again_button = ElevatedButton(" 🔄יאללה בוא ננסה שוב ", on_click=start_new_game, bgcolor=Colors.GREEN, color=Colors.WHITE)

    # סידור רכיבים במרכז המסך
    main_column = Column(
        [
            feedback_text,
            input_field,
            guess_button
        ],
        alignment="center",  # יישור אנכי במרכז
        horizontal_alignment="center",  # יישור אופקי במרכז
        spacing=20  # ריווח בין הרכיבים
    )

    # גם כדאי למרכז את כל התוכן של הדף
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"


    page.add(main_column)

flet.app(target=main, view=flet.WEB_BROWSER, port=8500)
