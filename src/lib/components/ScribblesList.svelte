<script>
  import PostPreview from '$lib/components/ScribblesPreview.svelte'
  import PostDate from '$lib/components/PostDate.svelte'

  export let posts
</script>

<div class="container grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-2 mx-auto items-center">
<!-- <div class="flex flex-col gap-20 grid-cols-4"> -->
  {#each posts as post}
    <!-- <article class="flex flex-col gap-20 grid-cols-4"> -->

        <PostPreview {post}>

        </PostPreview>

    <!-- </article> -->
  {/each}
  <!-- </div> -->
</div>

<style>
  .post-items{
    max-width: 100%;
  }
</style>
