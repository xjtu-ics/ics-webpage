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
        df.rename(columns={'start': 'Date','theme': 'Lecture', 'extra': "Labs", "pptLink" : "PPT"}, inplace=True)
        df['Date'] = pd.to_datetime(df['Date']).dt.date
        markdown_table = df.to_markdown(index=False, tablefmt="github")
        
        markdown_table = re.sub(
                r"(assets/slides/[^)]+\.pdf)",
                r"[:material-presentation-play: Slides](\1)",
                markdown_table
        )
        lines = markdown_table.split("\n")
        header = lines[0]
        separator = lines[1] 

        centered_separator = re.sub(r"(---+)", lambda x: f":{x.group(1)}:", separator)
        lines[1] = centered_separator

        centered_markdown_table = "\n".join(lines)        
        return centered_markdown_table