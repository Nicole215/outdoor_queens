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

Before deciding on marketing strategies and defining a business plan, I tried to answer the following questions to provide a framework for the business' strategy:
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

## Features
### Existing Features
The website is designed with a range of features to ensure a user-friendly and functional experience:

##### Responsive Navbar

- Includes a burger dropdown menu for seamless navigation on both desktop and mobile devices.
- Navigation options adapt based on user authentication (authorized users see personalized options).

![Screenshot 2024-12-15 120745](https://github.com/user-attachments/assets/d1d35e06-e67c-451b-9337-5cd26ff411a0)

![Screenshot 2024-12-15 120850](https://github.com/user-attachments/assets/d44847b9-9d12-4845-8ae9-59a21fca5286)

##### Footer

- Features links to social media platforms for easy engagement.
- Includes an email subscription form powered by MailChimp for optional newsletter sign-up.

![Screenshot 2024-12-15 121008](https://github.com/user-attachments/assets/77ee1ec6-6cee-456a-a76f-64d1743db9c5)

![Screenshot 2024-12-15 120958](https://github.com/user-attachments/assets/11019f37-0ee8-4739-8837-b9e305446f11)

##### Home Page

- Home Page with Hero Image
- Shop Now Button

![Screenshot 2024-12-15 121207](https://github.com/user-attachments/assets/b3e8765d-429f-4de4-bf5c-ef5c444b1d95)

##### FAQ Page

- Provides answers to common questions to assist users efficiently.
- Includes a contact form for users to reach out with specific queries.

![Screenshot 2024-12-15 121310](https://github.com/user-attachments/assets/132adb7a-e121-4e79-a4aa-2ceb301767fd)

![Screenshot 2024-12-15 121335](https://github.com/user-attachments/assets/f970dcd5-704d-4977-98e4-7131b999263b)

##### 404 Error Page

- Features the Hero Image as the background for a cohesive design.
- Notifies users of an invalid URL.
- Includes a Home Button that redirects users back to the Homepage for easy navigation.

![Screenshot 2024-12-15 121544](https://github.com/user-attachments/assets/aaeaebb7-aa36-420c-b1f6-614cacfea9f0)

#### Authentication
The website includes a robust authentication system to ensure secure user access:

##### Sign-Up Page

- Users can create an account by providing their details.
- A confirmation email with a verification link is sent to validate the account.

![Screenshot 2024-12-15 122157](https://github.com/user-attachments/assets/caec0428-6200-4efd-8919-acf2de2ca7a1)

![Screenshot 2024-12-15 122545](https://github.com/user-attachments/assets/630a4be8-b388-4398-ab48-a532810f76ad)

##### Login Page

- Registered users can log in securely to access personalized features.

![Screenshot 2024-12-15 122252](https://github.com/user-attachments/assets/ec0f15c6-9931-4aa6-8a2a-07691d61edd7)

![Screenshot 2024-12-15 122621](https://github.com/user-attachments/assets/7b1cfdb6-c7f1-49d2-99d0-9b1087eb693b)


##### Logout Functionality

- Users can log out easily, ensuring their account remains secure.

![Screenshot 2024-12-15 122652](https://github.com/user-attachments/assets/5d597a04-864e-4813-a0ba-60c7fcd1b3ea)

This system provides a smooth and secure user experience while maintaining data integrity.

#### Products
##### All Products Page
The Products Page is designed for easy browsing and navigation:

##### Shop Now Button

Located on the homepage, the "Shop Now" button directs users to a comprehensive view of all available products.

##### Category-Based Navigation

The responsive navbar allows users to filter products by category, enabling a more tailored shopping experience.
Categories include distinct groupings such as merchandise, event tickets, or other relevant product types.

![Screenshot 2024-12-15 123411](https://github.com/user-attachments/assets/869fe88e-5114-441b-a375-19b8f1e00354)

![Screenshot 2024-12-15 123443](https://github.com/user-attachments/assets/820022c3-31ce-4899-b6b7-1686b85506da)

![Screenshot 2024-12-15 123516](https://github.com/user-attachments/assets/8e69060b-89f6-4e0a-9dba-b39f57ecbf3d)

##### User-Friendly Layout

Products are displayed with clear images, descriptions, and prices, ensuring users can make informed decisions quickly.
Each product links to a dedicated page with additional details and purchase options.

![image](https://github.com/user-attachments/assets/46eb91c8-c78f-4291-9080-a444bc6ba2e8)

This intuitive structure ensures customers can effortlessly explore and find products that match their interests.

#### Add, Edit, and Delete Options
Authorized users have exclusive access to manage content through the following features:

##### Add New Products

Authorized users can add new products or events to the website, ensuring the offerings stay up-to-date.

![Screenshot 2024-12-15 130005](https://github.com/user-attachments/assets/642dd903-c2a6-4a3b-aace-91f4f35ae1ef)

![Screenshot 2024-12-15 130139](https://github.com/user-attachments/assets/32fc3ff7-a831-4bbe-a20e-6c7a672b774f)

##### Edit Existing Products

Allows authorized users to update product details such as names, descriptions, images, prices, or availability.

![Screenshot 2024-12-15 130226](https://github.com/user-attachments/assets/9c565285-ecb8-4514-aa8c-51135198cd32)

##### Delete Products

Products or events that are no longer relevant can be removed by authorized users, keeping the catalog streamlined and accurate.
These management features are restricted to authorized accounts, ensuring content control remains secure and aligned with the business objectives.

#### Search Bar
The website includes a fully functional search bar to enhance user navigation:

##### Quick Product Search

Users can easily search for products or events by entering relevant keywords.

#### Shopping Bag
##### Add to Bag
Users can add products to their shopping bag directly from the product page or search results.

![Screenshot 2024-12-15 130837](https://github.com/user-attachments/assets/d30447cc-6a4a-4c28-b7d9-ec3991b548d0)

![Screenshot 2024-12-15 130908](https://github.com/user-attachments/assets/cb8d61e9-ffbf-49c6-9960-cdd21c726d59)

##### View Bag
The shopping bag provides a summary of selected items, including product names, quantities, and prices, ensuring clarity before checkout.

![Screenshot 2024-12-15 131009](https://github.com/user-attachments/assets/092a9d5d-2780-4549-8dfe-e8a9737988ae)

##### Update or Remove Items
Users can adjust quantities or remove items from the shopping bag as needed, offering flexibility and control over their purchase.

##### Persistent Bag
The shopping bag contents remain saved during the session, allowing users to continue shopping without losing selected items.

##### Keep Shopping Button
A "Keep Shopping" button allows users to return to browsing without losing the items already added to their bag.

##### Proceed to Checkout
A clear "Checkout" button directs users to finalize their purchase with ease.

![Screenshot 2024-12-15 131041](https://github.com/user-attachments/assets/cf38b524-fc66-435b-acfb-382b3ff49e8f)

The shopping bag ensures a seamless and intuitive shopping experience, helping users review and manage their selections effortlessly.

#### Checkout Success Page
The website includes a dedicated Checkout Success Page to confirm and celebrate successful purchases:

##### Order Confirmation
Displays a clear confirmation message to reassure users that their order has been processed successfully.

![Screenshot 2024-12-15 131601](https://github.com/user-attachments/assets/22f2f7df-0e5c-4439-a77e-75a0ef92471d)

##### Order Details
Includes a summary of the order, such as purchased items, quantities, total amount paid, and an order reference number for tracking.

##### Next Steps
Provides guidance on what happens next, such as receiving a confirmation email or expected delivery timeline.

#### User Profile Page
The User Profile Page provides users with a centralized space to manage their personal information and view order history:

##### Contact Address Form
Includes a pre-populated form with the user's previously saved information for convenience.
Users can easily update their contact details when needed.

##### Update Information Button
A dedicated button allows users to save any changes made to their profile information.

##### Order History
Displays a list of the user's past orders, including order dates, items purchased, and total amounts.
Provides a convenient reference for tracking previous purchases.

![Screenshot 2024-12-15 132106](https://github.com/user-attachments/assets/c3efb1aa-29a7-4696-b5ee-172e74f67154)

## Possible Future Features
### Pre-Select Categories from Homepage
Future updates may include interactive buttons on the homepage for users to directly select product categories, such as "Get Tickets" and "Browse Merchandise." This will streamline navigation and help users quickly access the content they're interested in.

### Forum for Travel Buddies
A forum exclusively for logged-in users will be introduced, allowing customers to connect with like-minded individuals, share experiences, and find travel buddies for upcoming hikes, or mud runs. This feature will foster community engagement and provide added value to users planning group adventures.
