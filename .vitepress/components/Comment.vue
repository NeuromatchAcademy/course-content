<script setup lang="ts">
import { useData } from "vitepress";
import { onMounted, watch } from "vue";

const { isDark } = useData();

const loadUtterances = (useDarkTheme: boolean) => {
  const script = document.createElement("script");
  script.src = "https://utteranc.es/client.js";
  script.async = true;
  script.crossOrigin = "anonymous";
  script.setAttribute("repo", "FujishigeTemma/course-content-jp");
  script.setAttribute("issue-term", "pathname");
  script.setAttribute("label", "Comment");
  script.setAttribute("theme", useDarkTheme ? "github-dark" : "github-light");

  document.querySelector("#comment")!.replaceChildren(script);
};

onMounted(() => {
  loadUtterances(isDark.value);
});

watch(isDark, (value) => {
  loadUtterances(value);
});
</script>

<template>
  <div id="comment" />
</template>
