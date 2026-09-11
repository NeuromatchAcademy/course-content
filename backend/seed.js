// backend/seed.js
require('dotenv').config();
const mongoose = require('mongoose');
const connectDB = require('./config/db');
const Badge = require('./models/Badge');
const Quiz = require('./models/Quiz');
const Lesson = require('./models/Lesson');

const seed = async () => {
  await connectDB();

  // wipe everything
  await Promise.all([Badge.deleteMany(), Quiz.deleteMany(), Lesson.deleteMany()]);

  // ----------------- Badges -----------------
  const introBadge = await Badge.create({
    name: 'Neuro‑Intro Explorer',
    description: 'Completed the “Neuroscience Introduction” lesson',
    iconUrl: '/icons/intro.png',
    criteria: 'complete:neuro-intro'
  });

  const anatomyBadge = await Badge.create({
    name: 'Neuro‑Anatomist',
    description: 'Finished the Neuroanatomy lesson',
    iconUrl: '/icons/anatomy.png',
    criteria: 'complete:neuro-anatomy'
  });

  const quizBadge = await Badge.create({
    name: 'Quiz Whiz',
    description: 'Scored 100 % on the Intro Quiz',
    iconUrl: '/icons/quiz.png',
    criteria: 'pass:quiz-intro'
  });

  // ----------------- Lessons -----------------
  await Lesson.create([
    {
      slug: 'neuro-intro',
      title: 'Neuroscience Introduction',
      description: 'What is neuroscience? Scope, history, and key questions.',
      videoUrl: 'https://www.youtube.com/embed/5Xc6S45MZkM', // example YouTube embed
      markdownUrl: '/content/neuro-intro.md',
      badge: introBadge._id
    },
    {
      slug: 'neuro-anatomy',
      title: 'Neuroanatomy: Brain Regions',
      description: 'A tour of the cerebral cortex, subcortical nuclei and the spinal cord.',
      videoUrl: 'https://www.youtube.com/embed/6xwJbQYHc5U',
      markdownUrl: '/content/neuro-anatomy.md',
      badge: anatomyBadge._id
    }
  ]);

  // ----------------- Quizzes -----------------
  await Quiz.create({
    slug: 'quiz-intro',
    title: 'Intro Quiz',
    description: 'Test your basic neuroscience knowledge',
    badge: quizBadge._id,
    questions: [
      {
        prompt: 'Which of the following is NOT a major branch of neuroscience?',
        options: [
          { text: 'Cognitive neuroscience' },
          { text: 'Molecular neuroscience' },
          { text: 'Astrophysics' },
          { text: 'Computational neuroscience' }
        ],
        correctIndex: 2
      },
      {
        prompt: 'The cell body of a neuron is called the:',
        options: [
          { text: 'Axon' },
          { text: 'Dendrite' },
          { text: 'Soma' },
          { text: 'Myelin sheath' }
        ],
        correctIndex: 2
      }
    ]
  });

  console.log('✅ Seed complete – neuroscience data added');
  process.exit();
};

seed();
