<script setup lang="ts">
type Props = {
  href: string;
};

defineProps<Props>();
</script>

<template>
  <a target="_blank" :href="href" nofollow rel="noopener noreferrer">
    <img src="../../assets/colab_badge.svg" alt="Open In Colab" />
  </a>
</template>
