<script setup lang="ts">
type Props = {
  id: string;
};

defineProps<Props>();
</script>

<template>
  <iframe
    :class="$style.youtube"
    :src="`https://www.youtube.com/embed/${id}`"
    title="YouTube video player"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    allowfullscreen
  ></iframe>
</template>

<style module>
.youtube {
  width: 100%;
  aspect-ratio: 16/9;
}
</style>
