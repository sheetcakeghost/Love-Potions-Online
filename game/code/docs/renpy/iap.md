# In-App Purchasing

Ren'Py includes a high-level in-app purchasing framework. This framework currently only supports unlock-style purchases from the Apple App Store, Google Play, and the Amazon Appstore.

Using this framework is fairly simple, and consists of the following functions.

*   In the init phase of your game, register available purchases using the  function.
    
*   Once the game has started, check to see if a purchase has been purchased using the  function.
    
*   Allow the user to purchase an item using the  function or the  action.
    
*   Allow the user to restore purchases bought on other devices using the  function or the  action.
    

To offer in-app purchases, the purchases (including an associated price) must be set up on the various marketplaces.

## IAP Functions

iap.get\_price(_product_)

Returns a string giving the price of the product in the user's local currency. Returns None if the price of the product is unknown - which indicates the product cannot be purchased.

iap.get\_store\_name()

Returns the name of the enabled store for in-app purchase. This currently returns one of "amazon", "play" (for Google Play), "ios" or None if no store is available.

iap.has\_purchased(_product_)

Returns True if the user has purchased product in the past, and False otherwise.

iap.init()

Initialize iap. This should be called after all calls to iap.register(), but before any other iap function. If not called explicitly, this is automatically called at the end of the initialization phase.

iap.is\_deferred(_product_)

Returns True if the user has asked to purchase product, but that request has to be approved by a third party, such as a parent or guardian.

iap.purchase(_product_, _interact\=True_)

This function requests the purchase of product.

It returns true if the purchase succeeds, or false if the purchase fails. If the product has been registered as consumable, the purchase is consumed before this call returns.

iap.register(_product_, _identifier\=None_, _amazon\=None_, _google\=None_, _ios\=None_, _consumable\=False_)

Registers a product with the in-app purchase system.

product

A string giving the high-level name of the product. This is the string that will be passed to , , and  to represent this product.

identifier

A string that's used to identify the product internally. Once used to represent a product, this must never change. These strings are generally of the form "com.domain.game.product".

If None, defaults to product.

amazon

A string that identifies the product in the Amazon app store. If not given, defaults to identifier.

google

A string that identifies the product in the Google Play store. If not given, defaults to identifier.

ios

A string that identifies the product in the Apple App store for iOS. If not given, defaults to identifier.

consumable

True if this is a consumable purchase. Right now, consumable purchases are only supported on iOS.

iap.request\_review()

When called, the app store is asked to request a review from the user. This returns true if the request was successful, and false if the request was not. Note that a successful request does not mean that the user will be asked to review the app, as app stores determine if the user is actually asked.

This is supported on Google Play and the Apple App Store, only.

iap.restore(_interact\=True_)

Contacts the app store and restores any missing purchases.

interact

If True, renpy.pause will be called while waiting for the app store to respond.

## IAP Actions

iap.Purchase(_product_, _success\=None_)

An action that attempts the purchase of product. This action is sensitive if and only if the product is purchasable (a store is enabled, and the product has not already been purchased.)

success

If not None, this is an action or list of actions that are run when the purchase succeeds.

iap.Restore()

An Action that contacts the app store and restores any missing purchases.
