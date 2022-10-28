<script>
  import Card from './Card.svelte'

  export let post

  let stem = 'scribbles'

</script>

<Card href={`/${stem}/${post.slug}`} data-sveltekit-prefetch>
  <slot slot="eyebrow" name="eyebrow" />
  <slot slot="title">{post.title}</slot>
  <div slot="description" class="prose w-full rounded">
    
    <img src={`${post.preview.html}`} class="text-center">

  </div>
</Card>

<style>
  .prose > :global(p) {
    margin-top: 0;
    margin-bottom: 0;
  }
</style>
