<script setup lang="ts">
type Props = {
  id: string;
};

defineProps<Props>();
</script>

<template>
  <iframe
    class="w-full aspect-video"
    :src="`https://www.youtube.com/embed/${id}`"
    title="YouTube video player"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    allowfullscreen
  />
</template>
