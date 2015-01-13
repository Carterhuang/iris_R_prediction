data(iris)

library(DMwR)

model_map <- c()

species_set <- unique(iris$Species)
iris_category <- names(iris)

get_matrix <- function(data_set) {
    retrieve  <- function(n) {
        return (data_set[[n]])
    }
    return (sapply(names(data_set), retrieve))     
}

for (species in species_set) {
    sub_iris <- subset(iris, Species==species)
    sub_matrix <- get_matrix(sub_iris)
    for (i in 1:4) {
        key <- paste(iris_category[i], species, sep="%")
        index <- c(1:4)
        y <- sub_matrix[, i]
        x <- sub_matrix[,index[-i]]
        model_map[key] <- as.matrix(lm(y ~ x))
    }
}

predict_species <- function(Sepal.Length, Sepal.Width, Petal.Length, Petal.Width) {
    Species <- 'NULL'
    entry <- data.frame(Sepal.Length, Sepal.Width, Petal.Length, Petal.Width)
    nn15 <- kNN(Species ~ ., iris, entry, norm=TRUE, k=15)
    return (as.character(nn15))
}

predict_attribute <- function(predict_attr, input_species, Sepal.Length, 
                              Sepal.Width, Petal.Length, Petal.Width) {
    input <- c(1, Sepal.Length, Sepal.Width, Petal.Length, Petal.Width)
    key <- paste(predict_attr, input_species, sep="%")
    formula <- model_map[[key]]
    return (sum(formula * input))
}
