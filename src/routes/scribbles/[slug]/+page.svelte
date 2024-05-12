<script>
  import { format, parseISO } from 'date-fns'
  import { website, name} from '$lib/info.js'
  import ToC from '$lib/components/ToC.svelte'
  // import ArrowLeftIcon from '$lib/components/ArrowLeftIcon.svelte'
  // import SocialLinks from '$lib/components/SocialLinks.svelte'
  import { afterNavigate } from '$app/navigation'
  import Footy from '$lib/components/footer.svelte'

  /** @type {import('./$types').PageData} */
  export let data

  // generated open-graph image for sharing on social media.
  // see https://og-image.vercel.app/ for more options.
  const ogImage = `https://og-image.vercel.app/**${encodeURIComponent(
    data.post.title
  )}**?theme=light&md=1&fontSize=100px&images=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Ffront%2Fassets%2Fdesign%2Fhyper-color-logo.svg`

  const url = `${website}/${data.post.slug}`

  let showBackButton = false
  afterNavigate(({ from }) => {
    // only show back button if we navigated from within the site
    showBackButton = !!from
  })
</script>

<svelte:head>
  <title>{data.post.title} - {name}</title>
  <meta name="description" content={data.post.preview.text} />
  <meta name="author" content={name} />

  <!-- Facebook Meta Tags -->
  <meta property="og:url" content={url} />
  <meta property="og:type" content="website" />
  <meta property="og:title" content={data.post.title} />
  <meta property="og:description" content={data.post.preview.text} />
  <meta property="og:image" content={ogImage} />

  <!-- Twitter Meta Tags -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta property="twitter:domain" content={website} />
  <meta property="twitter:url" content={url} />
  <meta name="twitter:title" content={data.post.title} />
  <meta name="twitter:description" content={data.post.preview.text} />
  <meta name="twitter:image" content={ogImage} />
</svelte:head>

<div class="flex flex-col flex-grow w-full max-w-4xl mx-auto">
  <div class="relative w-full max-w-4xl">

    <article>
      <header class="flex flex-col">
        <h1
          class="text-center font-bold tracking-tight pb-10 sm:text-2xl"
        >
          {data.post.title}
        </h1>
        <!-- <div class="flex items-center order-first text-base text-zinc-400 dark:text-zinc-500"> -->
          <!-- <span class="h-4 w-0.5 rounded-full bg-zinc-200 dark:bg-zinc-500" /> -->
          <!-- <time dateTime={data.post.date}>
            <span class="ml-3">{format(new Date(parseISO(data.post.date)), 'MMMM d, yyyy')}</span>
          </time> -->
          <!-- <span class="mx-2">•</span> -->
          <!-- <span>{data.post.readingTime}</span> -->
        <!-- </div> -->
      </header>

      <!-- render the post -->
      <div class="">
        <svelte:component this={data.component} />
      </div>
    </article>

  </div>

  <!-- table of contents -->
  <div class="hidden xl:block">
    <aside class="sticky hidden w-48 ml-8 xl:block top-8" aria-label="Table of Contents">
      <ToC post={data.post} />
    </aside>
  </div>
</div>

<Footy/>