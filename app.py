import gradio as gr
import re

def translate_to_cli(user_instruction):
    # ניקוי רווחים והמרת הטקסט לבדיקה קלה
    text = user_instruction.lower().strip()
    
    # מילון חכם מבוסס ביטויים ותתי-מילים
    if re.search(r'(ip|כתובת)', text):
        return "ipconfig"
        
    elif re.search(r'(קובץ|קבצים|dir|רשימ)', text):
        return "dir"
        
    elif re.search(r'(נקה|לנקות|תנקה|cls|מסך)', text):
        return "cls"
        
    elif re.search(r'(חדש|תפתח תיקייה|mkdir|ליצור תיקייה)', text):
        return "mkdir malka_project"
        
    elif re.search(r'(מחק|למחוק|תמחק|del)', text):
        return "del old_notes.txt"
        
    elif re.search(r'(שעה|תאריך|זמן)', text):
        return "date /t && time /t"
        
    elif re.search(r'(תהליך|רצים|משימות|tasklist)', text):
        return "tasklist"
        
    elif re.search(r'(העתק|להעתיק|תעתיק|copy)', text):
        return "copy a.txt C:\\Users\\Desktop"
        
    elif re.search(r'(אינטרנט|רשת|פינג|ping)', text):
        return "ping google.com"
        
    elif re.search(r'(שם|rename|לשנות)', text):
        return "rename old.txt new.txt"
        
    elif re.search(r'(מעלה|אחורה|לצאת)', text):
        return "cd .."
        
    elif re.search(r'(טקסט|ליצור קובץ)', text):
        return "echo. > homework.txt"
        
    elif re.search(r'(כבה|לכבות|shutdown)', text):
        return "shutdown /s /t 60"
        
    elif re.search(r'(פרמט|לפרמט|format)', text):
        return "format C: /q"
        
    # אם המשתמש סתם כותב משהו לא קשור (כמו "שלום")
    return "UNKNOWN_COMMAND: Command not recognized by the system."

# בניית ממשק המשתמש עם Gradio
with gr.Blocks(title="Natural Language to CLI") as demo:
    gr.Markdown("# 🖥️ Natural Language to CLI Agent - MVP")
    gr.Markdown("שלב א': המרת שפה טבעית לפקודות טרמינל (Windows CMD) - סימולציה מקומית יציבה")
    
    with gr.Row():
        user_input = gr.Textbox(label="הוראה בשפה טבעית (לדוגמה: תראה לי את רשימת הקבצים בתיקייה)")
        generated_command = gr.Textbox(label="פקודת ה-CLI שנוצרה", interactive=False)
        
    submit_btn = gr.Button("תרגם לפקודה")
    submit_btn.click(fn=translate_to_cli, inputs=user_input, outputs=generated_command)

if __name__ == "__main__":
    demo.launch()