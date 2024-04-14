<script>
  import { name } from '$lib/info.js'
  // import ArrowLeftIcon from '$lib/components/ArrowLeftIcon.svelte'
  // import ArrowRightIcon from '$lib/components/ArrowRightIcon.svelte'
  import PostsList from '$lib/components/ScribblesList.svelte'



  let stem = 'scribbles'

  /** @type {import('./$types').PageData} */
  export let data

  // console.log(data)

  $: isFirstPage = data.page === 1
  $: hasNextPage = data.posts[data.posts.length - 1]?.previous
</script>

<svelte:head>
  <title>{name}</title>
</svelte:head>

<div class="flex flex-col flex-wrap flex-grow max-w-4xl mx-auto">

  <!-- <div class="container mx-auto px-4"> -->
    <!-- <div class='grid-cols-3 grid gap-3'> -->
    <PostsList posts={data.posts} />
  <!-- </div> -->
  <!-- </div> -->

  <!-- pagination -->
  <div class="flex items-center justify-between pt-10 text-xs">
    {#if !isFirstPage}
      <a class='pb-10' href={`/${stem}/page/${data.page - 1}`} data-sveltekit-prefetch>
        <!-- <ArrowLeftIcon class="w-4 h-4" /> -->
        Previous
      </a>
    {:else}
      <div />
    {/if}

    {#if hasNextPage}
      <a class='pb-10' href={`/${stem}/page/${data.page + 1}`} data-sveltekit-prefetch
        >Next
        <!-- <ArrowRightIcon class="w-4 h-4" /> -->
      </a>
    {/if}
  </div>
</div>

<style>
  a {
    @apply flex items-center gap-2 font-medium text-zinc-700;
  }

  :global(.dark) a {
    @apply text-zinc-300;
  }
</style>
