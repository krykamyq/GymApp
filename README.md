# GymApp

## Description
GymApp is a web application built using Django that helps users create personalized training plans and track their progress. It provides a user-friendly interface for individuals to set fitness goals, design training routines, monitor their workout performance, and assess their progress over time.

## Features
- User Registration: Allow new users to create an account and login to the application.
- Training Plan Creation: Create personalized training plans based on user's goals, fitness level, and preferences.
- Exercise Library: Access a comprehensive library of exercises with detailed descriptions, images, and video demonstrations.
- Workout Tracking: Track individual workouts by recording exercises, sets, repetitions, weights, and rest periods.
- Progress Tracking: Monitor progress over time through performance metrics such as weight lifted, repetitions completed, and workout duration.
- Goal Setting: Set short-term and long-term fitness goals, such as weight loss, muscle gain, or endurance improvement.
- Progress Assessment: Evaluate progress towards goals by comparing current performance with previous workout data.
- Data Visualization: Visualize progress through charts, graphs, and statistics to gain insights into performance trends.
- Customizable Reminders: Set reminders for scheduled workouts, rest days, or goal milestones.
- Social Interaction: Engage with a community of fitness enthusiasts, share achievements, and provide support to fellow users.
- Mobile Compatibility: Optimize the application for mobile devices, enabling users to track workouts and access features on the go.

## Installation
1. Clone the repository: `git clone https://github.com/krykamyq/GymApp.git
2. Change into the project directory: `cd gymapp`
3. Create a virtual environment: `python -m venv env`
4. Activate the virtual environment:
   - For Windows: `env\Scripts\activate`
   - For Unix/Linux: `source env/bin/activate`
5. Install the required dependencies: `pip install -r requirements.txt`
6. Configure the database settings in the `settings.py` file.
7. Apply migrations: `python manage.py migrate`
8. Create a superuser: `python manage.py createsuperuser`
9. Start the development server: `python manage.py runserver`

## Usage
1. Access the application by visiting `http://localhost:8000` in your web browser.
2. Register for a new account or login with your credentials.
3. Set your fitness goals and preferences to create a personalized training plan.
4. Explore the exercise library to find suitable exercises for your workouts.
5. Record your workouts by adding exercises, sets, repetitions, weights, and rest periods.
6. Track your progress over time and assess your performance towards achieving your goals.
7. Visualize your progress through charts and graphs to gain insights into your fitness journey.
8. Set reminders for scheduled workouts, rest days, or important milestones.
9. Connect with the community, share your achievements, and support others in their fitness endeavors.

## Contributing
Contributions are welcome! If you'd like to contribute to GymApp, please follow these steps:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Submit a pull request describing your changes.

## Acknowledgments
- The Django project: https://www.djangoproject.com/
- Other open-source libraries used in this project (see requirements.txt)