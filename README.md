# Outdoor Queens

This is a Django based (fictional!) e-commerce application which is the last of 5 required Code Institute portfolio projects.

Outdoor Queens offers a range of products, including tickets for hiking events, mud runs, and custom clothing & accessories. You can create an account to save your information, view order history, and purchase items. The site also features a contact form, FAQs, and an admin panel for managing the store's products.

![landingpage](https://github.com/user-attachments/assets/97884209-03eb-4497-aced-c31c701f75bc)

[Link to live site](https://outdoor-queens-e3117004e229.herokuapp.com/)

## UI/UX
The design of the site is intentionally simple and minimalistic, reflecting the essence of hiking and mud runs—where it's just you and nature. I wanted the user experience to be as straightforward and empowering as the adventures you embark on. The clean and uncluttered layout makes it easy to navigate, ensuring that users can focus on what matters most: their journey.

Additionally, the site features a subtle golden touch, symbolizing the sense of achievement and pride that comes with completing an event. Just like a successful hike or mud run, when you make it through, you look back and feel like a queen for what you've accomplished. This golden accent adds a feeling of triumph and celebration to every interaction.

## Agile
This project follows Agile principles to ensure a flexible, iterative approach to development. I break down tasks into manageable pieces, allowing for quick adjustments and continuous improvements based on feedback. The iterative nature of Agile helps keep the development process efficient and adaptable to changes.

To visualize and track progress, I use a Kanban board. The board provides a clear view of tasks at various stages, helping me stay organized and focused. Tasks are divided into columns such as:

- To Do: Tasks that need to be worked on.
- In Progress: Tasks currently being worked on.
- Done: Tasks that are completed and finalized.

## Wireframes
The initial wireframes are a simplified version of the finished product and merely served the purpose of listing the essential features.
<details>
<summary>Wireframe images</summary>
  
![landing page](https://github.com/user-attachments/assets/89b6ceef-a04b-4805-a406-95851a418842)

![product page](https://github.com/user-attachments/assets/a3193e6d-4272-4493-b80a-158d775f561a)

![FAQ and contact](https://github.com/user-attachments/assets/e9c1f3e8-163c-4043-a274-e6faec53d4ce)

</details>

## Plans of UX
#### Executive Summary
The Outdoor Queens E-Commerce Website aims to provide a seamless and user-friendly online experience for outdoor enthusiasts purchasing tickets for hiking events, mud runs, and custom merchandise. The goal is to create an intuitive interface that mirrors the simplicity and empowerment of outdoor adventures, while delivering an aesthetically pleasing experience that elevates users’ sense of accomplishment. With a focus on accessibility, ease of navigation, and visual appeal, the website will ensure customers enjoy a frictionless journey from browsing to purchase.

*Site owner:*
The owner of the site wants to be able to maintain the website without effort and via an appealing UI.

#### Objectives
1. **Enhance User Experience:** Build a website that reflects the spirit of outdoor adventures, ensuring the design is simple yet memorable, and easy to navigate for all users.
2. **Drive Conversions:** Ensure that users can easily browse events, purchase tickets, and explore merchandise, which will increase ticket sales and product purchases.
3. **Empower Users:** Implement a design that celebrates the sense of achievement after completing a hike or mud run, with special visual elements to make customers feel accomplished and rewarded.
4. **Increase Retention:** Provide account management features, allowing users to save their information, view order history, and return for future events with ease.

*Site owner:*
The owner of the site can easily add, edit or delete tickets and products via the front-end interface. This feature is only accessible to authorised users.

#### Target Audience
1. **Outdoor Enthusiasts:** Individuals passionate about hiking, mud runs, and outdoor activities, looking for a platform to book events and purchase related merchandise.
2. **Event Attendees:** Customers who are specifically looking for tickets to outdoor events such as hiking tours or mud runs.
3. **Merchandise Shoppers:** Customers interested in purchasing custom clothing and accessories that reflect their love for outdoor adventures.
4. **New Users & Returning Customers:** Users who will benefit from an account system that allows them to store personal information and track past purchases.

#### Design Philosophy
The design of the Hiking & Mud Run E-Commerce Website will reflect the following principles:

1. **Simplicity:** A minimalistic design that mirrors the purity of nature and outdoor experiences. Users should not feel overwhelmed by cluttered elements or excessive content.
2. **Intuitive Navigation:** Clear, simple navigation paths that guide users smoothly through ticket purchasing, merchandise shopping, and account management without confusion.
3. **Empowerment:** A visual design that incorporates elements symbolizing accomplishment. Golden accents are used to evoke a sense of pride and achievement, making users feel like they’ve conquered their journey.
4. **Accessibility:** The design follows best practices for accessibility, ensuring all users, regardless of ability, can easily access and navigate the site.

## Visual Design Choices
#### Color Scheme:
The overall page is hold in black and white. A darker gold (#DAA520) is used to highlight the character of achievment.

![Screenshot 2024-12-14 132426](https://github.com/user-attachments/assets/34d73dda-55ef-4b86-859f-7042dfa1749b)

#### Fonts:
For the websites typography, Lato was chosen because it is clean, yet modern.

#### Images and Icons:
For the design of the products, background and icons, a crown was chosen to represent achievements. The crown symbolizes the sense of accomplishment and triumph that comes after completing a challenging hike, mud run, or other endurance activity. This design element emphasizes the reward of perseverance and serves as a tribute to those who push their limits to achieve their goals.

## SEO and Marketing Research
### Keyword Research
#### Initial list of Keywords to research
- mud runs for women
- women only hiking events
- mud runs
- hiking events
- outdoor sports
- outdoor events for women
- mud run clothing for women
- obstacle races
- sporting women

### Research of similar businesses
As a hiker and mud runner myself, I got inspired by [Muddy Angels](https://www.muddyangelrun.com/) and [Mammutmarsch](https://mammutmarsch.de/).
During my keyword research on Google, I identified a few similar brands, primarily based in the United States. Most of these websites focus exclusively on either hiking events or mud runs. However, the integration of both activities into a single offering appears to be a unique value proposition, setting this concept apart in the market.

### SEO Improvements
#### Meta Tags
In the head of base.html, <meta name="description" ... and <meta name="keywords" ... tags were included.
#### Creating a sitemap
The sitemap file sitemap.xml was created using [XML Sitemaps](https://www.xml-sitemaps.com/) to enhance site navigation for search engines and accelerate content discovery. 
#### Creating a robots.txt file
The file specifies which directories search engines should avoid crawling and indexing, while also providing a link to the sitemap. Its presence demonstrates a level of site quality to search engines, contributing to improved SEO rankings.

### Marketing Strategies
#### Pre-strategy planning
The business operates on a B2C (business-to-consumer) model, focusing on delivering value directly to its customers. The core offerings include tickets for self-hosted events, such as hiking adventures and mud runs, as well as a range of branded merchandise. This dual revenue stream is designed to engage the target audience on multiple levels—providing unforgettable experiences while fostering brand loyalty through high-quality products.

<details>
<summary>Before deciding on marketing strategies and defining a business plan, I tried to answer the following questions to provide a framework for the business' strategy:</summary>
1. Who is my target audience?
   - **Who are the ideal customers for the events and merchandise?**
   - Outdoor enthusiasts, adventure seekers, fitness-minded individuals, and those who enjoy unique challenges like hiking and mud runs. Demographics might include people aged 18–105 with active lifestyles and disposable income.
2. What problem am I solving for my customers?
   - **How does the business meet the needs or desires of the target audience?**
   - Offering a combination of physical challenge and community connection through unique events, while providing memorable, high-quality merchandise that serves as a reward or memento.
3. What makes my business unique?
   - **What differentiates my offerings from competitors?**
   - The integration of hiking events and mud runs under one brand is unique, creating an unparalleled adventure experience. Additionally, the emphasis on branded merchandise strengthens emotional ties to the events.
4. How will I reach my audience?
   - **Which marketing channels are most effective?**
   - Leverage social media platforms like Instagram, Facebook, and TikTok to showcase event highlights and branded merchandise.
5. What are my goals for the business?
   - **What am I aiming to achieve in the short and long term?**
   - In the short term, generate buzz and ticket sales for events while growing social media following. Long-term goals include building a loyal community, expanding the merchandise line, and hosting larger events across multiple locations.
</details>

#### Strategies
- **Social Media Marketing**
  <details>
    <summary>Facebook mock page</summary>
    
    ![Facebook_Mockup](https://github.com/user-attachments/assets/7e3a7e08-edb5-43db-9c97-96b58a034a83)
  
  </details>

- **Email Marketing using MailChimp**
The MailChimp Newsletter subscription service is an excellent choice for a small-scale business like ours, as it is free and easy to set up. The newsletter content could include exclusive early access to event updates, promotions, and new merchandise announcements, reducing the time required for creating standalone marketing content. Subscribing to the newsletter is entirely optional for customers. On the site, the subscription form is subtly placed in the footer, avoiding the intrusive pop-up style commonly used on other websites.

![Screenshot 2024-12-14 160747](https://github.com/user-attachments/assets/0dcbabc4-8478-41f8-b9d5-77c3ae86cfc8)

![Screenshot 2024-12-14 160813](https://github.com/user-attachments/assets/72110914-ac28-42c6-8821-ddcb0d487908)

![Screenshot 2024-12-14 160824](https://github.com/user-attachments/assets/1cc484f9-3032-4fa5-aa5a-58349b2bb572)


