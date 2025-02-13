---
hide:
  - toc
  - navigation
---
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>staff</title>
    <style>
        .md-content__inner > h1 {
            display: none;
        }
        body {
            background-image: url('/assets/background.png');
            background-repeat: no-repeat;
            background-position: 5% 30%;
            background-size: cover;
            display: flex;
        }

        [data-md-color-scheme="slate"] .md-main {
            background: linear-gradient(
                rgba(0, 0, 0, 0.88),
                rgba(0, 0, 0, 0.88)
            ),
            url('/assets/background.png') center/cover fixed !important;
        }

        .md-tabs {
            background-color: rgba(255, 255, 255, 0) !important;
        }

        .md-header {
            background-color: rgba(255, 255, 255, 0) !important;
            backdrop-filter: blur(4px);
        }

        [data-md-color-scheme="slate"] .md-nav {
            background-color: rgba(0, 0, 0, 0.86) !important;
        }

        .frosted-glass {
            width: 900px;
            height: 400px;
            background: rgba(255, 255, 255, 0.2);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            position: absolute;
            top: 40%;
            left: 50%;
            transform: translate(-50%, -50%);
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            color: white;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            padding: 20px;
            box-sizing: border-box;
        }

        .frosted-glass div {
            margin: 1px 0;
            text-align: center;
        }

        .frosted-glass div:first-child {
            font-size: 60px;
            font-weight: bold;
        }

        .frosted-glass div:nth-child(2) {
            font-size: 60px;
            font-weight: bold;
        }

        .frosted-glass div:nth-child(3) {
            font-size: 50px;
            margin-top: 15px;
        }
    </style>
</head>

<body>
    <div class="frosted-glass">
        <div>XJTU COMP400727</div>
        <div>FALL 2025</div>
        <div>Introduction to Computer Systems</div>
    </div>
</body>

</html>