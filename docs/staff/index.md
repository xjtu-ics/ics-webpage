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
    <title>Staff</title>
    <link rel="stylesheet" href="../stylesheets/staff.css">
</head>
<body>

    <script>
        document.addEventListener('DOMContentLoaded', function () {
            // 封装通用的加载函数
            const loadProfiles = (url, targetElementId) => {
                const targetElement = document.getElementById(targetElementId);
                fetch(url)
                    .then(response => response.json())
                    .then(data => {
                        data.forEach(item => {
                            const nameHtml = item.homepage_url
                                ? `<a href="${item.homepage_url}">${item.name}</a>`
                                : `<span>${item.name}</span>`;
                            const email = item.email
                                ? `<div class="profile-email">${item.email}</div>`
                                : ``
                            const office = item.office
                                ? `<div class="profile-office">${item.office}</div>`
                                : ``
                            const intro = item.intro
                                ? `<div class="profile-intro">${item.intro}</div>`
                                : ``
                            const template = `
                                <div class="profile-card">
                                    <img 
                                        src="${item.pic_url}" 
                                        alt="none" 
                                        class="profile-image"
                                    >
                                    <div class="profile-info">
                                        <div class="profile-name">${nameHtml}</div>
                                        ${email}
                                        ${office}
                                        ${intro}
                                    </div>
                                </div>
                            `;
                            targetElement.insertAdjacentHTML('beforeend', template);
                        });
                    })
                    .catch(error => console.error(`加载 ${targetElementId} JSON 文件失败:`, error));
            };

            loadProfiles('../static/data/profile-inst.json', 'profile-inst');
            loadProfiles('../static/data/profile-ta.json', 'profile-ta');
        });
    </script>
</body>
</html>

# **Staff**

## **Instructors**

<div id="profile-inst">
</div>

## **TAs**

<div id="profile-ta">
</div>
