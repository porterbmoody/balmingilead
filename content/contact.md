---
title: Contact
featured_image: '/images/snake.jpg'
omit_header_text: true
description: YO!!
type: page
menu: main

---



{{<form-contact action="https://example.com">}}
  Your name:
  <input type="text" name="name" required>
  Your email:
  <input type="email" name="email" required>
  Your message:
  <textarea name="message" required></textarea>
  <input type="submit" value="Send message">
{{</form-contact>}}