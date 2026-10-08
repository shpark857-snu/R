args <- commandArgs(trailingOnly = TRUE)
input <- if (length(args) >= 1L) args[[1L]] else "data/kettle-bom.csv"

bom <- read.csv(input, check.names = FALSE, stringsAsFactors = FALSE)
required <- c("material", "finished_mass_g", "scope")
stopifnot(identical(names(bom), required))
stopifnot(nrow(bom) == 12L)
stopifnot(!anyNA(bom), all(nzchar(bom$material)))
stopifnot(is.numeric(bom$finished_mass_g), all(is.finite(bom$finished_mass_g)))
stopifnot(all(bom$finished_mass_g > 0))
stopifnot(setequal(unique(bom$scope), c("Kettle", "Packaging")))

kettle_g <- sum(bom$finished_mass_g[bom$scope == "Kettle"])
packaging_g <- sum(bom$finished_mass_g[bom$scope == "Packaging"])
stopifnot(isTRUE(all.equal(kettle_g, 723)))
stopifnot(isTRUE(all.equal(packaging_g, 137.8)))

cat(sprintf("Kettle: %.2f g\nPackaging: %.2f g\nPackaged: %.2f g\n",
            kettle_g, packaging_g, kettle_g + packaging_g))
