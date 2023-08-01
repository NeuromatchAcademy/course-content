<script setup lang="ts">
import { useData } from "vitepress";
import Theme from "vitepress/theme";
import Comment from "../components/Comment.vue";
import LinkToOriginal from "../components/LinkToOriginal.vue";
import OpenInColab from "../components/OpenInColab.vue";

const { Layout } = Theme;

const { page, frontmatter } = useData();
</script>

<template>
  <Layout>
    <template #aside-bottom>
      <div class="w-full flex justify-center">
        <LinkToOriginal
          v-if="frontmatter.original"
          :href="frontmatter.original"
        />
      </div>
    </template>

    <template #doc-before>
      <div class="w-full flex mb-4">
        <OpenInColab v-if="frontmatter.colab" :href="frontmatter.colab" />
      </div>
    </template>

    <template #doc-footer-before>
      <Comment v-if="!frontmatter.disableComment" :key="page.relativePath" />
    </template>
  </Layout>
</template>
