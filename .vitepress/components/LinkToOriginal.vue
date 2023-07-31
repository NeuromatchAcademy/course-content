<script setup lang="ts">
type Props = {
  href: string;
};

defineProps<Props>();
</script>

<template>
  <a
    class="h-6 block flex items-center gap-2 px-8 py-4 rounded"
    nofollow
    :href="href"
    target="_blank"
    rel="noreferrer noopener"
  >
    <span>原文で読む</span>
    <span class="i-material-symbols-open-in-new h-6 w-6" />
  </a>
</template>
