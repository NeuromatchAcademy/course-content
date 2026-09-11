// backend/models/Lesson.js
const mongoose = require('mongoose');

const LessonSchema = new mongoose.Schema(
  {
    slug: { type: String, required: true, unique: true }, // e.g. "intro-to-modeling"
    title: { type: String, required: true },
    description: { type: String },
    // you can store a YouTube ID, Vimeo URL, or a markdown file path
    videoUrl: { type: String },          // optional video
    markdownUrl: { type: String },       // optional rich‑text lesson content
    // which badge (if any) is granted when the lesson is marked complete
    badge: { type: mongoose.Schema.Types.ObjectId, ref: 'Badge' }
  },
  { timestamps: true }
);

module.exports = mongoose.model('Lesson', LessonSchema);
