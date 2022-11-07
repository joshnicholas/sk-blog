<script>
  import Card from './Linkcard.svelte'

  export let post
  // console.log("postal", post)
  // console.log("postal", post.preview.link)
</script>

<Card data-sveltekit-prefetch="off">
  <slot slot="eyebrow" name="eyebrow" />
  <slot slot="title">{post.title}</slot>
  <div slot="description" class="prose dark:prose-invert">
    {@html post.preview.html}
  </div>
  <div slot="actions">
    <!-- <div class="flex items-center text-teal-500"> -->
      <!-- <span class="text-sm font-medium">Read</span> -->
      <!-- <ArrowRightIcon class="w-4 h-4 ml-1" /> -->
      <p class='linko'>
        <a href='{post.preview.link}' data-sveltekit-prefetch="off" rel="noreferrer" target="_blank">Read more...</a></p>
  
    <!-- </div> -->
  </div>
  <hr>
</Card>

<style>
  .prose > :global(p) {
    margin-top: 0;
    margin-bottom: 0;
  }


  a {
    color: #84cc16
  }
</style>
