def contractText(contractInfo) :
    members = ", ".join(contractInfo["members"])
    return f"""Entre les soussignés :Wild Pulse Management, représenté par Charlie Spirit, domiciliée à Montélimar, ci-après dénommé « Le Manager », 

Et Le groupe {contractInfo["groupName"]}, composé de {members}, domicilié à {contractInfo["groupAdress"]}, ci-après dénommé « L’Artiste ». 

Article 1 - Le présent contrat a pour objet de définir les termes et conditions de la collaboration entre le Manager et l’Artiste, concernant la représentation, la gestion et la promotion du groupe {contractInfo["groupName"]}. 

Article 2 - Engagements du Manager.
    Le Manager s’engage à : 

    Représenter l’Artiste dans la recherche et la négociation de contrats de concerts, festivals et autres événements musicaux,

    Assurer la promotion et la communication du groupe sur les plateformes adéquates, 

    Conseiller l’Artiste sur sa stratégie de développement et son image publique. 

Article 3 - Engagements de l’Artiste
    L’Artiste s’engage à : 

    Fournir au Manager tout le matériel promotionnel nécessaire (photos, biographie, enregistrements, etc.),

    Être disponible pour les concerts et engagements pris par le Manager,

    Ne pas signer de contrat avec un autre manager sans en informer Wild Pulse Management.

Article 4 - Durée - Le présent contrat est conclu pour une durée de 2 ans à compter du {contractInfo["contractDate"]}. Il est renouvelable par tacite reconduction sauf notification écrite d’une des parties {contractInfo["preavis"]} avant expiration.

Article 5 - Conditions financières - Le Manager percevra {contractInfo["commission"]}% des revenus générés par l’Artiste pour les prestations obtenues par son intermédiaire. Ce paiement sera effectué par virement.

Article 6 - Résiliation - Le contrat pourra être résilié par l’une ou l’autre des parties sous réserve d’un préavis de {contractInfo["preavis"]}, par courrier recommandé avec accusé de réception. 

Article 7 - Conditions spécifiques -
{contractInfo["specificConditions"]}


    """