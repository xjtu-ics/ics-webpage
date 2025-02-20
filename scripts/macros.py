import pandas as pd
import re
def define_env(env):
    @env.macro
    def read_csv(csv_path):
        df = pd.read_csv(csv_path)
        df["theme"].fillna("TBA", inplace=True)
        df.fillna('', inplace=True)
        # only select Lecture
        df = df[df['title'] == 'Lecture']
        df = df.drop(columns=['title', 'end', 'location'])
        df.rename(columns={'start': 'Date','theme': 'Lecture', 'extra': "Labs", "pptLink" : "Materials"}, inplace=True)
        df['Materials'] = df['Materials'].apply(lambda str: f"[:material-presentation-play: Slides]({str}){{.md-button}}" if str != "" else "")
        df['Date'] = pd.to_datetime(df['Date']).dt.date
        markdown_table = df.to_markdown(index=False, tablefmt="github")
        
        lines = markdown_table.split("\n")
        header = lines[0]
        separator = lines[1] 

        centered_separator = re.sub(r"(---+)", lambda x: f":{x.group(1)}:", separator)
        lines[1] = centered_separator

        centered_markdown_table = "\n".join(lines)        
        return centered_markdown_table