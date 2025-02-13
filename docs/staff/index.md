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
    <style></style>
</head>

<body>
    <script>
        document.addEventListener('DOMContentLoaded', function () {
            fetch('../static/data/profile-inst.json')
               .then(response => response.json())
               .then(data => {
                    const targetElement = document.getElementById('instructors');
                    data.forEach(item => {
                        const nameHtml = item.homepage_url
                           ? `<a href="${item.homepage_url}">${item.name}</a>`
                            : `<span>${item.name}</span>`;
                        const template = `
                            <div style="display: flex; align-items: center; padding: 16px; border: 1px solid #e0e0e0; border-radius: 8px; margin-bottom: 16px; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); transition: box-shadow 0.3s ease;">
                                <img 
                                    src="${item.pic_url}" 
                                    alt="加载失败" 
                                    style="width: 96px; height: 96px; border-radius: 50%; object-fit: cover; margin-right: 20px; border: 2px solid #f0f0f0;"
                                >
                                <div style="flex: 1;">
                                    <div style="flex: 1;">
                                        <h3 style="font-size: 24px; font-weight: 600; color: #333; margin: 0 0 1px;">${nameHtml}</h3>
                                        <p style="font-size: 16px; color: #666; margin: 0 0 1px;">${item.email}</p>
                                        <p style="font-size: 16px; color: #666; margin: 0 0 1px;">${item.office}</p>
                                        <p style="font-size: 16px; color: #666; margin: 0;">${item.intro}</p>
                                    </div>
                                </div>
                            </div>
                        `;
                        targetElement.insertAdjacentHTML('beforeend', template);
                    });
                })
               .catch(error => console.error('加载教师 JSON 文件失败:', error));
            fetch('../static/data/profile-ta.json')
               .then(response => response.json())
               .then(data => {
                    const targetElement = document.getElementById('tas');
                    data.forEach(item => {
                        const nameHtml = item.homepage_url
                           ? `<a href="${item.homepage_url}">${item.name}</a>`
                            : `<span>${item.name}</span>`;
                        const template = `
                            <div style="display: flex; align-items: center; padding: 16px; border: 1px solid #e0e0e0; border-radius: 8px; margin-bottom: 16px; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); transition: box-shadow 0.3s ease;">
                                <img 
                                    src="${item.pic_url}" 
                                    alt="加载失败" 
                                    style="width: 96px; height: 96px; border-radius: 50%; object-fit: cover; margin-right: 20px; border: 2px solid #f0f0f0;"
                                >
                                <div style="flex: 1;">
                                    <h3 style="font-size: 24px; font-weight: 600; color: #333; margin: 0 0 1px;">${nameHtml}</h3>
                                    <p style="font-size: 16px; color: #666; margin: 0 0 1px;">${item.email}</p>
                                    <p style="font-size: 16px; color: #666; margin: 0 0 1px;">${item.office}</p>
                                    <p style="font-size: 16px; color: #666; margin: 0;">${item.intro}</p>
                                </div>
                            </div>
                        `;
                        targetElement.insertAdjacentHTML('beforeend', template);
                    });
                })
               .catch(error => console.error('加载助教 JSON 文件失败:', error));
        });
    </script>
</body>

</html>

# **Staff**

## **Instructors**

## **TAs**