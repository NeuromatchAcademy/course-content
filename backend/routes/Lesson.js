// backend/routes/lesson.js
const express = require('express');
const protect = require('../middleware/auth');
const Lesson = require('../models/Lesson');
const Badge = require('../models/Badge');
const router = express.Router();

// PUBLIC – list all lessons (titles only)
router.get('/', async (req, res) => {
  const lessons = await Lesson.find().select('-markdownUrl -videoUrl');
  res.json(lessons);
});

// PUBLIC – get lesson details (including video/markdown URLs)
router.get('/:slug', async (req, res) => {
  const lesson = await Lesson.findOne({ slug: req.params.slug }).populate('badge');
  if (!lesson) return res.status(404).json({ message: 'Lesson not found' });
  res.json(lesson);
});

// PROTECTED – mark lesson as completed (adds to user.completedLessons)
router.post('/:slug/complete', protect, async (req, res) => {
  const lesson = await Lesson.findOne({ slug: req.params.slug }).populate('badge');
  if (!lesson) return res.status(404).json({ message: 'Lesson not found' });

  const user = await require('../models/User').findById(req.user.id);
  if (!user.completedLessons.includes(lesson.slug)) {
    user.completedLessons.push(lesson.slug);
    // award badge if lesson has one
    if (lesson.badge) {
      const alreadyHas = user.earnedBadges.some(
        (b) => b.toString() === lesson.badge._id.toString()
      );
      if (!alreadyHas) user.earnedBadges.push(lesson.badge._id);
    }
    await user.save();
  }

  res.json({
    completedLessons: user.completedLessons,
    earnedBadges: user.earnedBadges
  });
});

module.exports = router;
