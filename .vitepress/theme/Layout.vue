<script setup lang="ts">
import { useData } from "vitepress";
import Theme from "vitepress/theme";
import Comment from "../components/Comment.vue";

const { Layout } = Theme;

const { page, frontmatter } = useData();
</script>

<template>
  <Layout>
    <template #doc-top></template>

    <template #doc-footer-before>
      <Comment v-if="!frontmatter.disableComment" :key="page.relativePath" />
    </template>
  </Layout>
</template>
