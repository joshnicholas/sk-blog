<script>
  import PostPreview from '$lib/components/WordsPreview.svelte'
  import PostDate from '$lib/components/PostDate.svelte'

  export let posts
</script>

<div class="flex flex-col gap-10">
  {#each posts as post}
    <article class=" ">
      <!-- <PostDate class="flex-col hidden md:flex" {post} /> -->

      <!-- <div class="col-span-4 md:col-span-3"> -->
        <PostPreview {post}>
          <!-- <slot slot="eyebrow">
            <PostDate class="md:hidden" {post} collapsed decorate />
          </slot> -->
        </PostPreview>
      <!-- </div> -->
    </article>
  {/each}
</div>

<style>
  .post-items{
    max-width: 100%;
  }
</style>
