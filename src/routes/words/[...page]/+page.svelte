<script>
  import { name } from '$lib/info.js'
  // import ArrowLeftIcon from '$lib/components/ArrowLeftIcon.svelte'
  // import ArrowRightIcon from '$lib/components/ArrowRightIcon.svelte'
  import PostsList from '$lib/components/WordsList.svelte'



  /** @type {import('./$types').PageData} */
  export let data

  $: isFirstPage = data.page === 1
  $: hasNextPage = data.posts[data.posts.length - 1]?.previous
</script>

<svelte:head>
  <title>{name}</title>
</svelte:head>

<div class="flex flex-col flex-grow max-w-4xl mx-auto">

  <!-- <div class="mt-16 sm:mt-20"> -->
    <PostsList posts={data.posts} />
  <!-- </div> -->

  <!-- pagination -->
  <div class="pb-10 flex items-center justify-between  pt-10 text-xs">
    {#if !isFirstPage}
      <a href={`/words/page/${data.page - 1}`} data-sveltekit-prefetch>
        <!-- <ArrowLeftIcon class="w-4 h-4" /> -->
        Previous
      </a>
    {:else}
      <div />
    {/if}

    {#if hasNextPage}
      <a href={`/words/page/${data.page + 1}`} data-sveltekit-prefetch
        >Next
        <!-- <ArrowRightIcon class="w-4 h-4" /> -->
      </a>
    {/if}
  </div>
</div>

<style>
  a {
    @apply flex items-center gap-2 font-medium;
  }


</style>
