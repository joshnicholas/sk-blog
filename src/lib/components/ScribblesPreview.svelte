<script>
  import Card from './Card.svelte'

  export let post

  let stem = 'scribbles'

</script>

<Card href={`/${stem}/${post.slug}`}>
  <slot slot="eyebrow" name="eyebrow" />
  <slot slot="title">{post.title}</slot>
  <div slot="description" class=" w-full">
    
    <img src={`${post.preview.html}`} class="text-center rounded-2xl">

  </div>
</Card>

<!-- <style>
  .prose > :global(p) {
    margin-top: 0;
    margin-bottom: 0;
  }
</style> -->
